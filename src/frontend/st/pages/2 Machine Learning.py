import os
from datetime import datetime

import streamlit as st
from backend.data_processing.alphavantage_processed import get_processed_table
import numpy as np
import pandas as pd
from backend.database.users_database import get_user_table, list_user_tables
from backend.database.db_functions import get_all_yf_price_history, get_yf_pricing_raw
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
    accuracy_score,
    ConfusionMatrixDisplay,
)
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import joblib

# __________________________ Konfiguration __________________________

MODEL_DIR = "saved_models"
os.makedirs(MODEL_DIR, exist_ok=True)

ALPHAVANTAGE_TABLES = [
    "alphavantage_pricing_processed",
    "alphavantage_processed_kpi",
]

ALPHA_PRICING_TABLE = "alphavantage_pricing_processed"
ALPHA_KPI_TABLE = "alphavantage_processed_kpi"

# __________________________Header____________________________

st.set_page_config(
    page_title="Machine Learning Playground",
    page_icon="🧠",
    layout="wide"
)
# ____________________________________________________________


# ---------------------- Helper-Funktionen ----------------------

@st.cache_data
def load_data_from_source(
    source: str,
    symbol: str = None,
    table_name: str = None,
):
    """
    Lädt Daten je nach ausgewählter Quelle mit deinen bestehenden Funktionen.
    """
    if source == "YF_PRICE_HISTORY (alle Symbole)":
        df = get_all_yf_price_history()

    elif source == "YF_PRICING_RAW (Symbol)":
        if not symbol:
            return pd.DataFrame()
        df = get_yf_pricing_raw(symbol)

    elif source == "Alphavantage (einzeln)":
        if not table_name:
            return pd.DataFrame()
        df = get_processed_table(table_name)

    elif source == "Alphavantage (Pricing + KPI kombiniert)":
        # beide Tabellen aus engine holen
        df_price = get_processed_table(ALPHA_PRICING_TABLE)
        df_kpi = get_processed_table(ALPHA_KPI_TABLE)

        # symbol + timestamp in beiden DataFrames als Join-Keys vorbereiten
        if "symbol" not in df_price.columns or "symbol" not in df_kpi.columns:
            return pd.DataFrame()

        # timestamp-Feld in beiden Tabellen auf datetime casten (falls als String gespeichert)
        if "timestamp" in df_price.columns:
            df_price["timestamp"] = pd.to_datetime(df_price["timestamp"])
        else:
            return pd.DataFrame()

        if "timestamp" in df_kpi.columns:
            df_kpi["timestamp"] = pd.to_datetime(df_kpi["timestamp"])
        else:
            return pd.DataFrame()

        join_cols = ["symbol", "timestamp"]

        # Inner Join: nur Zeilen, die in beiden Tabellen vorkommen
        df = pd.merge(
            df_price,
            df_kpi,
            on=join_cols,
            how="inner",
            suffixes=("_price", "_kpi"),
        )

    elif source == "User-Tabelle (users_database)":
        if not table_name:
            return pd.DataFrame()
        df = get_user_table(table_name)

    else:
        df = pd.DataFrame()

    return df


def detect_time_column(df: pd.DataFrame):
    """
    Versucht automatisch die Zeitspalte zu identifizieren.
    Priorität:
    1. Spalte mit Namen 'date'
    2. Spalten mit datetime64 dtype
    3. Spaltennamen, die 'date', 'time' oder 'timestamp' enthalten
    """
    cols = df.columns.tolist()

    # 1. explizit "date"
    if "date" in cols:
        return "date"

    # 2. echte Datetime-Spalten
    datetime_cols = [c for c in cols if np.issubdtype(df[c].dtype, np.datetime64)]
    if datetime_cols:
        return datetime_cols[0]

    # 3. heuristisch nach Namen
    keywords = ["date", "time", "timestamp"]
    for c in cols:
        if any(k in c.lower() for k in keywords):
            return c

    return None


def make_future_target(df: pd.DataFrame, time_col: str, target_col: str, horizon_label: str):
    """
    Erzeugt ein zukünftiges Target auf Basis einer Zeitspalte.
    y_future(t) = y(t + delta) wird auf die Zeile mit Zeitpunkt t gemappt.
    """
    df = df.copy()
    if not np.issubdtype(df[time_col].dtype, np.datetime64):
        df[time_col] = pd.to_datetime(df[time_col])

    df = df.sort_values(time_col)

    if horizon_label == "1 Tag":
        delta = pd.DateOffset(days=1)
        suffix = "1d"
    elif horizon_label == "3 Wochen":
        delta = pd.DateOffset(weeks=3)
        suffix = "3w"
    elif horizon_label == "3 Monate":
        delta = pd.DateOffset(months=3)
        suffix = "3m"
    else:
        # Kein Shift → nichts verändern
        return df, target_col

    future_col = f"{target_col}_future_{suffix}"

    tmp = df[[time_col, target_col]].copy()
    tmp[time_col] = tmp[time_col] - delta
    tmp = tmp.rename(columns={target_col: future_col})

    merged = df.merge(tmp, on=time_col, how="left")
    merged = merged.dropna(subset=[future_col])

    return merged, future_col


def make_lag_features(df: pd.DataFrame, time_col: str, base_col: str, n_lags: int):
    """
    Erzeugt Lag-Features aus einer Basis-Spalte.
    Beispiel: base_col = 'close', n_lags = 3
    → close_lag_1, close_lag_2, close_lag_3
    """
    df = df.copy()

    if time_col not in df.columns:
        raise ValueError(f"Zeitspalte '{time_col}' nicht im DataFrame gefunden.")

    if base_col not in df.columns:
        raise ValueError(f"Basis-Spalte '{base_col}' nicht im DataFrame gefunden.")

    # Zeitspalte in echtes Datetime-Format bringen und sortieren
    if not np.issubdtype(df[time_col].dtype, np.datetime64):
        df[time_col] = pd.to_datetime(df[time_col])

    df = df.sort_values(time_col)

    # Basis-Spalte numerisch machen (falls Strings)
    df[base_col] = pd.to_numeric(df[base_col], errors="coerce")

    lag_cols = []
    for lag in range(1, n_lags + 1):
        col_name = f"{base_col}_lag_{lag}"
        df[col_name] = df[base_col].shift(lag)
        lag_cols.append(col_name)

    return df, lag_cols


def preprocess_features_target_regression(df: pd.DataFrame, feature_cols, target_col, scale: bool):
    """
    Preprocessing für Regression:
    - Target -> float
    - numerische Feature-Spalten (auch String -> float)
    - One-Hot-Encoding für echte Kategoricals
    - optionales Scaling
    """
    df = df.copy()

    # ---- Target konvertieren ----
    if target_col not in df.columns:
        raise ValueError(f"Target-Spalte '{target_col}' nicht im DataFrame gefunden.")

    df[target_col] = pd.to_numeric(df[target_col], errors="coerce")

    # ---- Features extrahieren ----
    missing_features = [c for c in feature_cols if c not in df.columns]
    if missing_features:
        raise ValueError(f"Folgende Feature-Spalten fehlen im DataFrame: {missing_features}")

    X_raw = df[feature_cols].copy()

    numeric_feature_cols = []
    categorical_feature_cols = []

    for col in X_raw.columns:
        s = X_raw[col]
        if pd.api.types.is_numeric_dtype(s):
            numeric_feature_cols.append(col)
        else:
            # Versuche numerisch zu interpretieren
            converted = pd.to_numeric(s, errors="coerce")
            non_na_ratio = converted.notna().mean()

            # Heuristik: wenn >70% konvertierbar → als numerisch behandeln
            if non_na_ratio > 0.7:
                X_raw[col] = converted
                numeric_feature_cols.append(col)
            else:
                categorical_feature_cols.append(col)

    X_num = X_raw[numeric_feature_cols] if numeric_feature_cols else pd.DataFrame(index=df.index)
    X_cat = X_raw[categorical_feature_cols] if categorical_feature_cols else pd.DataFrame(index=df.index)

    if not X_cat.empty:
        X_cat_dummies = pd.get_dummies(X_cat, drop_first=True)
    else:
        X_cat_dummies = X_cat

    X_full = pd.concat([X_num, X_cat_dummies], axis=1)

    data = pd.concat([X_full, df[target_col]], axis=1)
    data = data.dropna()
    if data.empty:
        raise ValueError("Nach dem Bereinigen (NaNs entfernen) sind keine Datenzeilen mehr übrig.")

    y_clean = data[target_col]
    X_clean = data.drop(columns=[target_col])

    scaler = None
    if scale and not X_clean.empty:
        scaler = StandardScaler()
        X_used = scaler.fit_transform(X_clean)
    else:
        X_used = X_clean.values

    return X_used, y_clean, X_clean, scaler


def preprocess_features_target_classification(df: pd.DataFrame, feature_cols, target_col, scale: bool):
    """
    Preprocessing für Klassifikation (Logistische Regression):
    - Target als Klassen (LabelEncoder)
    - Features analog wie bei Regression (numerisch/kategorial)
    """
    df = df.copy()

    if target_col not in df.columns:
        raise ValueError(f"Target-Spalte '{target_col}' nicht im DataFrame gefunden.")

    # ---- Features ----
    missing_features = [c for c in feature_cols if c not in df.columns]
    if missing_features:
        raise ValueError(f"Folgende Feature-Spalten fehlen im DataFrame: {missing_features}")

    X_raw = df[feature_cols].copy()

    numeric_feature_cols = []
    categorical_feature_cols = []

    for col in X_raw.columns:
        s = X_raw[col]
        if pd.api.types.is_numeric_dtype(s):
            numeric_feature_cols.append(col)
        else:
            converted = pd.to_numeric(s, errors="coerce")
            non_na_ratio = converted.notna().mean()
            if non_na_ratio > 0.7:
                X_raw[col] = converted
                numeric_feature_cols.append(col)
            else:
                categorical_feature_cols.append(col)

    X_num = X_raw[numeric_feature_cols] if numeric_feature_cols else pd.DataFrame(index=df.index)
    X_cat = X_raw[categorical_feature_cols] if categorical_feature_cols else pd.DataFrame(index=df.index)

    if not X_cat.empty:
        X_cat_dummies = pd.get_dummies(X_cat, drop_first=True)
    else:
        X_cat_dummies = X_cat

    X_full = pd.concat([X_num, X_cat_dummies], axis=1)

    # ---- Target ----
    y_raw = df[target_col].astype(str)
    data = pd.concat([X_full, y_raw.rename(target_col)], axis=1)
    data = data.dropna()
    if data.empty:
        raise ValueError("Nach dem Bereinigen (NaNs entfernen) sind keine Datenzeilen mehr übrig.")

    y_labels = data[target_col].astype(str)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y_labels)

    X_clean = data.drop(columns=[target_col])

    scaler = None
    if scale and not X_clean.empty:
        scaler = StandardScaler()
        X_used = scaler.fit_transform(X_clean)
    else:
        X_used = X_clean.values

    return X_used, y_encoded, X_clean, scaler, label_encoder


def save_model_bundle(
    model,
    algo_name: str,
    data_source: str,
    feature_cols,
    target_col: str,
    scaler,
    horizon_label: str,
    label_encoder=None,
    time_series_mode: bool = False,
    n_lags: int | None = None,
    base_col: str | None = None,
):
    """
    Speichert Modell + Metadaten als .pkl in MODEL_DIR.
    """
    ts_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_algo = algo_name.replace(" ", "")
    safe_target = target_col.replace(" ", "_").replace("/", "_")

    filename = f"{safe_algo}__{safe_target}__{ts_str}.pkl"
    filepath = os.path.join(MODEL_DIR, filename)

    bundle = {
        "model": model,
        "algo": algo_name,
        "data_source": data_source,
        "feature_cols": list(feature_cols),
        "target_col": target_col,
        "scaler": scaler,
        "horizon": horizon_label,
        "label_encoder": label_encoder,
        "time_series_mode": time_series_mode,
        "n_lags": n_lags,
        "lag_base_col": base_col,
        "saved_at": ts_str,
    }

    joblib.dump(bundle, filepath)
    return filepath


# --------------------------- UI ---------------------------

st.markdown(
    """
    <style>
    .big-title {
        font-size: 2.3rem;
        font-weight: 700;
    }
    .subtitle {
        font-size: 1rem;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="big-title">🧠 Machine Learning Playground</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Baue schnell eigene Modelle auf Basis deiner Finanz- & User-Daten. '
    'Wähle Algorithmus, Datenquelle, Features & Target – der Playground übernimmt den Rest.</p>',
    unsafe_allow_html=True,
)

st.divider()

# --------------------------- Sidebar ---------------------------

with st.sidebar:
    st.header("⚙️ Einstellungen")

    algo = st.selectbox(
        "Algorithmus",
        [
            "Lineare Regression",
            "Decision Tree",
            "Random Forest",
            "Klassifikation (Logistische Regression)",
            "Richtungsklassifikation (LogReg, Up/Down)",
        ]
    )

    data_source = st.selectbox(
        "Datenquelle",
        [
            "YF_PRICE_HISTORY (alle Symbole)",
            "YF_PRICING_RAW (Symbol)",
            "Alphavantage (einzeln)",
            "Alphavantage (Pricing + KPI kombiniert)",
            "User-Tabelle (users_database)"
        ]
    )

    symbol = None
    table_name = None

    if data_source == "YF_PRICING_RAW (Symbol)":
        symbol = st.text_input("Symbol (z.B. AAPL, MSFT)", value="AAPL")

    elif data_source == "Alphavantage (einzeln)":
        table_name = st.selectbox(
            "Alphavantage-Tabelle",
            ALPHAVANTAGE_TABLES
        )

    elif data_source == "User-Tabelle (users_database)":
        user_tables = list_user_tables()
        if user_tables:
            table_name = st.selectbox("User-Tabelle auswählen", user_tables)
        else:
            st.warning("Keine Tabellen in users_database gefunden.")
            table_name = None

    test_size = st.slider(
        "Test Set Größe",
        min_value=0.1,
        max_value=0.5,
        value=0.2,
        step=0.05
    )

    scale_features = st.checkbox(
        "Features skalieren (StandardScaler)",
        value=True,
        help="Empfohlen vor allem für lineare Modelle und Logistische Regression."
    )

    # Zeitreihenmodus
    use_time_series = st.checkbox(
        "Zeitreihenmodus (Lag-Features vom Target)",
        value=False,
        help="Erzeugt automatisch Lag-Features der Target-Spalte (z.B. close_lag_1 ... close_lag_n) "
             "und nutzt diese als Input für das Modell."
    )

    if use_time_series:
        n_lags = st.slider(
            "Anzahl vergangener Zeitpunkte (Lags)",
            min_value=1,
            max_value=30,
            value=5,
            help="Wie viele vergangene Werte der Target-Spalte als Features genutzt werden sollen."
        )
    else:
        n_lags = None

    train_button = st.button("🚀 Modell trainieren")


# ---------------------- Daten laden & Spaltenwahl ----------------------

df = load_data_from_source(data_source, symbol=symbol, table_name=table_name)

if df is None or df.empty:
    st.warning("Noch keine Daten geladen oder Filter ergeben ein leeres DataFrame.")
else:
    st.subheader("📊 Datenvorschau")

    with st.expander("DataFrame anzeigen", expanded=True):
        st.dataframe(df.head(50), width="stretch")

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    all_cols = df.columns.tolist()

    st.markdown("#### 🔧 Feature & Target Auswahl")

    col1, col2 = st.columns([2, 1])

    with col1:
        feature_cols = st.multiselect(
            "Feature-Spalten (X)",
            options=all_cols,
            default=[c for c in numeric_cols if c != "target"][:5]
        )

    with col2:
        # Target darf auch bei den Features dabei sein (für Zeit-Shift & Lags)
        target_col = st.selectbox(
            "Target-Spalte (y)",
            options=all_cols,
        )

    # ---------------- Zukunfts-Target Einstellungen ----------------

    st.markdown("#### ⏩ Vorhersagehorizont (Zukunfts-Target)")

    auto_time_col = detect_time_column(df)

    if auto_time_col is None:
        st.warning("⚠️ Keine geeignete Zeitspalte erkannt. Zukunfts-Target (Shift) ist deaktiviert.")
        time_col = None
        horizon_label = "Kein Shift (aktuelles Target)"
    else:
        time_col = st.selectbox(
            "Zeitspalte für zukünftiges Target",
            options=[auto_time_col] + [c for c in all_cols if c != auto_time_col],
            index=0,
            help="Automatisch erkannte Zeitspalte, um das Target in die Zukunft zu verschieben."
        )
        horizon_label = st.selectbox(
            "Vorhersagehorizont",
            [
                "Kein Shift (aktuelles Target)",
                "1 Tag",
                "3 Wochen",
                "3 Monate"
            ],
            index=0
        )

    # Hinweis bei möglichem Leakage (nur für Regression kritisch)
    if (algo not in ["Klassifikation (Logistische Regression)", "Richtungsklassifikation (LogReg, Up/Down)"]
            and target_col in feature_cols
            and horizon_label == "Kein Shift (aktuelles Target)"
            and not use_time_series):
        st.warning(
            "Hinweis: Die Target-Spalte ist auch als Feature ausgewählt **ohne** Zeithorizont-Shift. "
            "Das kann zu Data Leakage führen. Mit Zeit-Shift oder Zeitreihenmodus ist das normalerweise unkritisch."
        )

    if train_button:
        if not feature_cols and not use_time_series:
            st.error("Bitte wähle mindestens eine Feature-Spalte aus (oder aktiviere den Zeitreihenmodus).")
        elif not target_col:
            st.error("Bitte wähle eine Target-Spalte aus.")
        else:
            try:
                with st.spinner("Training in Progress..."):
                    df_for_model = df.copy()

                    # Zeilenlimit, damit dir der RAM nicht explodiert
                    MAX_ROWS = 20000
                    if len(df_for_model) > MAX_ROWS:
                        st.warning(
                            f"Dataset hat {len(df_for_model)} Zeilen – es werden nur die ersten {MAX_ROWS} "
                            f"Zeilen zum Training verwendet."
                        )
                        df_for_model = df_for_model.head(MAX_ROWS)

                    # 1) Zukunfts-Target erzeugen (falls gewünscht)
                    if horizon_label != "Kein Shift (aktuelles Target)":
                        if time_col is None:
                            st.error("Es wurde keine gültige Zeitspalte erkannt. Shift des Targets ist nicht möglich.")
                            st.stop()
                        df_for_model, effective_target_col = make_future_target(
                            df_for_model, time_col, target_col, horizon_label
                        )
                        st.info(
                            f"Zukunfts-Target erzeugt: '{effective_target_col}' basiert auf '{target_col}' "
                            f"mit Horizont '{horizon_label}'."
                        )
                    else:
                        effective_target_col = target_col

                    # 1a) Richtungsklassifikation: binary Target bauen (Up/Down)
                    is_directional_cls = (algo == "Richtungsklassifikation (LogReg, Up/Down)")
                    if is_directional_cls:
                        if effective_target_col == target_col:
                            st.error(
                                "Richtungsklassifikation benötigt einen Vorhersagehorizont "
                                "(z.B. 1 Tag, 3 Wochen, 3 Monate)."
                            )
                            st.stop()

                        # numerisch machen und Up/Down berechnen
                        current_vals = pd.to_numeric(df_for_model[target_col], errors="coerce")
                        future_vals = pd.to_numeric(df_for_model[effective_target_col], errors="coerce")
                        df_for_model["direction_up"] = (future_vals > current_vals).astype(int)
                        effective_target_col = "direction_up"

                        st.info(
                            "Richtungsklassifikation aktiv: "
                            "Target = 1, wenn Future-Preis > aktueller Preis, sonst 0."
                        )

                    # 2) Zeitreihenmodus: Lag-Features aus Target bauen
                    active_feature_cols = feature_cols.copy()

                    if use_time_series:
                        if time_col is None:
                            st.error("Zeitreihenmodus benötigt eine gültige Zeitspalte.")
                            st.stop()

                        df_for_model, lag_cols = make_lag_features(
                            df_for_model,
                            time_col=time_col,
                            base_col=target_col,
                            n_lags=n_lags,
                        )
                        active_feature_cols = lag_cols

                        st.info(
                            f"Zeitreihenmodus aktiv: Verwende die Lag-Features {lag_cols[:3]} ... "
                            f"(insgesamt {len(lag_cols)}) als Input."
                        )

                    # Klassifikation vs. Regression
                    is_classification = algo in [
                        "Klassifikation (Logistische Regression)",
                        "Richtungsklassifikation (LogReg, Up/Down)",
                    ]

                    if is_classification:
                        X_used, y, X_encoded, scaler, label_encoder = preprocess_features_target_classification(
                            df_for_model,
                            active_feature_cols,
                            effective_target_col,
                            scale=scale_features,
                        )
                    else:
                        X_used, y, X_encoded, scaler = preprocess_features_target_regression(
                            df_for_model,
                            active_feature_cols,
                            effective_target_col,
                            scale=scale_features,
                        )
                        label_encoder = None

                    if X_used.shape[0] < 5:
                        st.warning(
                            f"Nur {X_used.shape[0]} Zeilen nach Preprocessing übrig – "
                            f"das ist sehr wenig zum Trainieren."
                        )

                    X_train, X_test, y_train, y_test = train_test_split(
                        X_used,
                        y,
                        test_size=test_size,
                        random_state=42,
                        shuffle=not use_time_series,
                    )

                    st.success(f"Trainingsdaten vorbereitet: X_train={X_train.shape}, X_test={X_test.shape}")

                    # ---------------------- Modelltraining ----------------------

                    if is_classification:
                        # Logistische Regression für Klassifikation
                        model = LogisticRegression(max_iter=1000)
                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)

                        if is_directional_cls:
                            st.markdown("### 🎯 Ergebnisse – Richtungsklassifikation (Up/Down)")
                            algo_name_for_save = "Richtungsklassifikation (LogReg)"
                        else:
                            st.markdown("### 🎯 Ergebnisse – Klassifikation (Logistische Regression)")
                            algo_name_for_save = "Logistische Regression (Klassifikation)"

                        acc = accuracy_score(y_test, y_pred)
                        st.metric("Accuracy", f"{acc:.4f}")

                        fig, ax = plt.subplots()
                        ConfusionMatrixDisplay.from_predictions(y_test, y_pred, ax=ax)
                        ax.set_title("Konfusionsmatrix")
                        st.pyplot(fig)

                    else:
                        # Regressionsmodelle
                        if algo == "Lineare Regression":
                            model = LinearRegression()
                            algo_name_for_save = "Lineare Regression"
                        elif algo == "Decision Tree":
                            model = DecisionTreeRegressor(random_state=42)
                            algo_name_for_save = "Decision Tree (Regression)"
                        else:  # Random Forest
                            model = RandomForestRegressor(
                                n_estimators=200,
                                random_state=42
                            )
                            algo_name_for_save = "Random Forest (Regression)"

                        model.fit(X_train, y_train)
                        y_pred = model.predict(X_test)

                        st.markdown(f"### 📈 Ergebnisse – {algo_name_for_save}")

                        mse = mean_squared_error(y_test, y_pred)
                        rmse = np.sqrt(mse)
                        r2 = r2_score(y_test, y_pred)

                        m1, m2, m3 = st.columns(3)
                        m1.metric("RMSE", f"{rmse:.4f}")
                        m2.metric("MSE", f"{mse:.4f}")
                        m3.metric("R²", f"{r2:.4f}")

                        st.line_chart(
                            pd.DataFrame({"y_true": y_test, "y_pred": y_pred}).reset_index(drop=True)
                        )

                    # ---------------------- Modell speichern ----------------------
                    save_path = save_model_bundle(
                        model=model,
                        algo_name=algo_name_for_save,
                        data_source=data_source,
                        feature_cols=active_feature_cols,
                        target_col=effective_target_col,
                        scaler=scaler,
                        horizon_label=horizon_label,
                        label_encoder=label_encoder,
                        time_series_mode=use_time_series,
                        n_lags=n_lags,
                        base_col=target_col if use_time_series else None,
                    )

                    st.success(f"Modell gespeichert unter: `{save_path}`")
                    st.caption("Du kannst diese .pkl-Datei in einem anderen Tab laden und für neue Vorhersagen nutzen.")

            except Exception as e:
                st.error(f"Fehler beim Training oder bei der Auswertung: {e}")