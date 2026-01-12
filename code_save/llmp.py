# file: src/backend/launch.py
import os
import time
import requests
import streamlit as st
import pandas as pd
import numpy as np
from backend.data_processing.alphavantage_processed import get_processed_table
from backend.database.users_database import get_user_table, list_user_tables
from backend.database.db_functions import get_all_yf_price_history, get_yf_pricing_raw

# __________________________Header____________________________

st.set_page_config(page_title="LLM Playground", page_icon="🤖", layout="wide")

# -----------------------------
# Hilfsfunktionen - Ollama
# -----------------------------
def base_url_from_choice(choice: str, custom: str | None = None) -> str:
    if choice == "Container":
        return "http://ollama:11434"
    if choice == "Host":
        return "http://host.docker.internal:11434"
    if choice == "Local" and custom:
        return custom.strip().rstrip("/")
    return os.environ.get("OLLAMA_HOST", "http://localhost:11434")


def check_connection(base_url: str, timeout: float = 3.0) -> tuple[bool, str]:
    """Prüft, ob Ollama am base_url erreichbar ist."""
    try:
        r = requests.get(f"{base_url}/api/version", timeout=timeout)
        if r.ok:
            return True, f"Verbunden mit Ollama @ {base_url} (Version: {r.json().get('version', 'unbekannt')})"
        return False, f"Keine OK-Antwort von {base_url} (Status {r.status_code})"
    except Exception as e:
        return False, f"Keine Verbindung zu {base_url}: {e}"


def ensure_model(base_url: str, model: str, timeout: float = 120.0) -> None:
    """Sorgt dafür, dass ein Modell vorhanden ist."""
    try:
        resp = requests.post(
            f"{base_url}/api/pull",
            json={"name": model, "stream": False},
            timeout=timeout,
        )
    except Exception as e:
        st.info(f"Modell '{model}' konnte nicht automatisch geladen werden: {e}")


def generate_once(base_url: str, model: str, prompt: str, timeout: float = 120.0) -> str:
    """Einmalige Textgenerierung (keine Streaming-Antwort)."""
    r = requests.post(
        f"{base_url}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=timeout,
    )
    r.raise_for_status()
    data = r.json()
    return data.get("response", "")


# -----------------------------
# Hilfsfunktionen - Daten
# -----------------------------
def _try_parse_numeric_series(s: pd.Series) -> pd.Series | None:
    """Versucht, eine String-Serie robust in floats umzuwandeln."""
    s = s.astype(str).str.strip()
    s = s.replace({"": np.nan, "-": np.nan, "NA": np.nan, "NaN": np.nan})

    frac_digit = s.str.contains(r"\d", regex=True).mean()
    if frac_digit < 0.5:
        return None

    s_clean = (
        s.str.replace("%", "", regex=False)
         .str.replace("€", "", regex=False)
         .str.replace("$", "", regex=False)
         .str.replace(" ", "", regex=False)
    )

    cand1 = pd.to_numeric(s_clean, errors="coerce")
    s_de = s_clean.str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
    cand2 = pd.to_numeric(s_de, errors="coerce")

    ratio1 = cand1.notna().mean()
    ratio2 = cand2.notna().mean()

    best_ratio = max(ratio1, ratio2)
    if best_ratio < 0.5:
        return None

    return cand1 if ratio1 >= ratio2 else cand2


def auto_convert_numeric_and_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """Konvertiert String-Spalten in float/datetime."""
    df = df.copy()

    for col in df.columns:
        col_series = df[col]

        if pd.api.types.is_numeric_dtype(col_series) or np.issubdtype(col_series.dtype, np.datetime64):
            continue

        col_lower = col.lower()

        if any(k in col_lower for k in ["date", "time", "timestamp"]):
            dt = pd.to_datetime(col_series, errors="coerce", infer_datetime_format=True)
            if dt.notna().mean() > 0.5:
                df[col] = dt
                continue

        parsed = _try_parse_numeric_series(col_series)
        if parsed is not None:
            df[col] = parsed

    return df


@st.cache_data
def load_data_from_source(
    source: str,
    symbol: str = None,
    table_name: str = None,
):
    """Lädt Daten je nach ausgewählter Quelle."""
    if source == "Price History":
        df = get_all_yf_price_history()
    elif source == "Single Stock Price":
        if not symbol:
            return pd.DataFrame()
        df = get_yf_pricing_raw(symbol)
    elif source == "Alphavantage":
        if not table_name:
            return pd.DataFrame()
        df = get_processed_table(table_name)
    elif source == "User Tables":
        if not table_name:
            return pd.DataFrame()
        df = get_user_table(table_name)
    else:
        df = pd.DataFrame()

    if df is not None and not df.empty:
        df = auto_convert_numeric_and_datetime(df)

    return df


def build_prediction_prompt(
    prediction_type: str,
    df: pd.DataFrame,
    feature_cols: list,
    target_col: str,
    sample_size: int = 10
) -> str:
    """Erstellt den Prompt für das LLM basierend auf Vorhersagetyp und Daten."""
    
    # Datensample vorbereiten
    df_sample = df[feature_cols + [target_col]].tail(sample_size)
    data_str = df_sample.to_string(index=False)
    
    # Statistiken
    stats_str = df[feature_cols + [target_col]].describe().to_string()
    
    # Basis-Prompt je nach Typ
    if prediction_type == "Regression (Zahlenwert vorhersagen)":
        prompt = f"""Du bist ein Finanzanalyst mit Expertise in quantitativer Analyse. 

AUFGABE: Analysiere die folgenden Finanzdaten und erstelle eine fundierte Vorhersage für '{target_col}'.

VERFÜGBARE FEATURES:
{', '.join(feature_cols)}

AKTUELLE DATEN (letzte {sample_size} Zeilen):
{data_str}

STATISTIKEN:
{stats_str}

ANWEISUNG:
1. Analysiere die Trends und Muster in den Features
2. Identifiziere relevante Korrelationen mit dem Target '{target_col}'
3. Gib eine konkrete numerische Vorhersage für den nächsten Wert von '{target_col}'
4. Begründe deine Vorhersage kurz und prägnant
5. Nenne ein Konfidenzintervall (min-max Bereich)

FORMAT:
Vorhersage: [Zahlenwert]
Konfidenzintervall: [min] - [max]
Begründung: [Deine Analyse]"""

    elif prediction_type == "Klassifikation (Kategorie vorhersagen)":
        unique_values = df[target_col].unique()[:10]
        prompt = f"""Du bist ein Finanzanalyst mit Expertise in Klassifikationsaufgaben.

AUFGABE: Analysiere die folgenden Daten und klassifiziere den nächsten Wert von '{target_col}'.

VERFÜGBARE FEATURES:
{', '.join(feature_cols)}

MÖGLICHE KATEGORIEN FÜR '{target_col}':
{', '.join(map(str, unique_values))}

AKTUELLE DATEN (letzte {sample_size} Zeilen):
{data_str}

STATISTIKEN:
{stats_str}

ANWEISUNG:
1. Analysiere die Muster in den Features
2. Identifiziere, welche Features die Klassifikation beeinflussen
3. Wähle die wahrscheinlichste Kategorie für den nächsten Wert
4. Begründe deine Wahl mit konkreten Beobachtungen aus den Daten
5. Gib Wahrscheinlichkeiten für die Top-3 Kategorien an (falls möglich)

FORMAT:
Vorhersage: [Kategorie]
Wahrscheinlichkeit: [Prozent]
Alternative Kategorien: [Kategorie 2] ([Prozent]), [Kategorie 3] ([Prozent])
Begründung: [Deine Analyse]"""

    elif prediction_type == "Trend-Analyse (Richtung vorhersagen)":
        prompt = f"""Du bist ein Finanzanalyst mit Expertise in Trendanalyse.

AUFGABE: Analysiere die Trends und sage vorher, ob '{target_col}' steigen, fallen oder stabil bleiben wird.

VERFÜGBARE FEATURES:
{', '.join(feature_cols)}

AKTUELLE DATEN (letzte {sample_size} Zeilen):
{data_str}

STATISTIKEN:
{stats_str}

ANWEISUNG:
1. Identifiziere den aktuellen Trend in '{target_col}'
2. Analysiere, wie die Features den Trend beeinflussen
3. Sage vorher, ob der Trend sich fortsetzt, umkehrt oder stagniert
4. Klassifiziere als: STEIGEND, FALLEND oder STABIL
5. Begründe deine Vorhersage mit Momentum-Indikatoren und Feature-Analyse

FORMAT:
Trend-Vorhersage: [STEIGEND/FALLEND/STABIL]
Konfidenz: [Hoch/Mittel/Niedrig]
Erwartete Änderung: [Prozent oder absoluter Wert]
Begründung: [Deine Analyse mit technischen Indikatoren]"""

    else:  # Freie Analyse
        prompt = f"""Du bist ein Finanzanalyst mit breiter Expertise.

AUFGABE: Führe eine umfassende Analyse der folgenden Daten durch.

VERFÜGBARE FEATURES:
{', '.join(feature_cols)}

TARGET VARIABLE:
{target_col}

AKTUELLE DATEN (letzte {sample_size} Zeilen):
{data_str}

STATISTIKEN:
{stats_str}

ANWEISUNG:
1. Analysiere die Datenqualität und Vollständigkeit
2. Identifiziere Muster, Trends und Anomalien
3. Untersuche Korrelationen zwischen Features und Target
4. Gib Einschätzungen zur Vorhersagbarkeit
5. Empfehle weitere Analyseschritte oder Feature Engineering

Erstelle eine strukturierte, detaillierte Analyse."""

    return prompt


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🤖 LLM Playground mit Datenanalyse")

st.caption("""
Nutze Ollama-LLMs für intelligente Finanzanalysen und Vorhersagen basierend auf deinen Daten.
""")

# -----------------------------
# Sidebar: Ollama-Konfiguration
# -----------------------------
with st.sidebar:
    st.header("⚙️ Ollama Einstellungen")
    
    choice = st.radio(
        "Quelle wählen:",
        options=["Container", "Host", "Local"],
        index=0,
        horizontal=True,
    )

    custom_url = None
    if choice == "Local":
        custom_url = st.text_input("Local Ollama URL:", value="http://localhost:11434")

    base_url = base_url_from_choice(choice, custom_url)
    st.code(base_url, language=None)

    if st.button("🔌 Verbindung testen"):
        ok, msg = check_connection(base_url)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

    st.divider()
    
    model = st.text_input("Modellname:", value="mathstral:7b")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔽 Load Model"):
            with st.spinner(f"Lade Modell '{model}'..."):
                ensure_model(base_url, model, timeout=120)
                st.success(f"✓ Modell '{model}' geladen!")
    with col_b:
        timeout_s = st.number_input("Timeout (s)", min_value=5, max_value=600, value=120, help="Timeout bestimmt wie lange auf die Antwort des Modells gewartet wird (sollte beim Download erhöht werden)")
    
    auto_pull = st.toggle("Auto-Load bei Analyse", value=True, 
                          help="Modell automatisch laden, wenn nicht vorhanden")

    st.divider()
    
    # Datenquelle
    st.header("📊 Datenquelle")
    
    data_source = st.selectbox(
        "Datenquelle",
        [
            "No Table selected",
            "Price History",
            "Single Stock Price",
            "Alphavantage",
            "User Tables",
        ]
    )

    symbol = None
    table_name = None

    if data_source == "Single Stock Price":
        symbol = st.text_input("Symbol (z.B. AAPL)", value="AAPL")
    elif data_source == "No Table selected":
        st.info("Wähle eine Tabelle")
    elif data_source == "Alphavantage":
        ALPHAVANTAGE_TABLES = [
            "alphavantage_pricing_processed",
            "alphavantage_processed_kpi",
        ]
        table_name = st.selectbox("Alphavantage-Tabelle", ALPHAVANTAGE_TABLES)
    elif data_source == "User Tables":
        user_tables = list_user_tables()
        if user_tables:
            table_name = st.selectbox("User Table", user_tables)
        else:
            st.warning("Keine Tabellen gefunden")
            table_name = None

# -----------------------------
# Hauptbereich: Datenauswahl & Analyse
# -----------------------------

# Daten laden
with st.spinner("Lade Daten..."):
    df = load_data_from_source(data_source, symbol=symbol, table_name=table_name)

if df is None or df.empty:
    st.warning("⚠️ Keine Daten geladen. Bitte wähle eine Datenquelle aus.")
    st.stop()

# Datenübersicht
st.subheader("📊 Datenübersicht")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Zeilen", len(df))
with c2:
    st.metric("Spalten", df.shape[1])
with c3:
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    st.metric("Numerische Spalten", len(numeric_cols))

with st.expander("📋 DataFrame anzeigen", expanded=False):
    st.dataframe(df.head(50), width="stretch")

# Feature & Target Auswahl
st.divider()
st.subheader("🎯 Feature & Target Auswahl")

all_cols = df.columns.tolist()

col1, col2 = st.columns([2, 1])

with col1:
    feature_cols = st.multiselect(
        "Feature-Spalten (X)",
        options=all_cols,
        default=[c for c in numeric_cols if c != "target"][:5],
        help="Wähle die Spalten, die als Input für die Analyse dienen sollen"
    )

with col2:
    target_col = st.selectbox(
        "Target-Spalte (y)",
        options=all_cols,
        help="Die Variable, die vorhergesagt werden soll"
    )

# Vorhersage-Konfiguration
st.divider()
st.subheader("🔮 Vorhersage-Konfiguration")

col_pred1, col_pred2 = st.columns(2)

with col_pred1:
    prediction_type = st.selectbox(
        "Vorhersagetyp",
        [
            "Regression (Zahlenwert vorhersagen)",
            "Klassifikation (Kategorie vorhersagen)",
            "Trend-Analyse (Richtung vorhersagen)",
            "Freie Analyse",
        ],
        help="Wähle, welche Art von Analyse das LLM durchführen soll"
    )

with col_pred2:
    sample_size = st.slider(
        "Datensample-Größe",
        min_value=5,
        max_value=50,
        value=10,
        help="Anzahl der letzten Zeilen, die ans LLM gesendet werden"
    )

# Benutzerdefinierter Prompt (optional)
with st.expander("✏️ Benutzerdefinierten Prompt hinzufügen (optional)"):
    custom_prompt_addition = st.text_area(
        "Zusätzliche Anweisungen für das LLM:",
        placeholder="z.B.: Berücksichtige besonders makroökonomische Faktoren...",
        height=100
    )

# Generieren Button
st.divider()

if not feature_cols:
    st.warning("⚠️ Bitte wähle mindestens eine Feature-Spalte aus.")
elif not target_col:
    st.warning("⚠️ Bitte wähle eine Target-Spalte aus.")
else:
    if st.button("🪄 LLM-Analyse starten", type="primary", width="stretch"):
        # Verbindung prüfen
        ok, msg = check_connection(base_url)
        if not ok:
            st.error(f"❌ Kann nicht verbinden: {msg}")
            st.stop()
        
        st.success(msg)
        
        # Modell laden
        if auto_pull:
            with st.status(f"Lade Modell '{model}'...", expanded=False) as status:
                ensure_model(base_url, model, timeout=timeout_s)
                status.update(label=f"✓ Modell '{model}' bereit", state="complete")
        
        # Prompt erstellen
        with st.spinner("Erstelle Analyse-Prompt..."):
            base_prompt = build_prediction_prompt(
                prediction_type=prediction_type,
                df=df,
                feature_cols=feature_cols,
                target_col=target_col,
                sample_size=sample_size
            )
            
            if custom_prompt_addition:
                full_prompt = f"{base_prompt}\n\nZUSÄTZLICHE ANWEISUNGEN:\n{custom_prompt_addition}"
            else:
                full_prompt = base_prompt
        
        # Prompt anzeigen (optional)
        with st.expander("📝 Generierter Prompt anzeigen"):
            st.code(full_prompt, language="text")
        
        # Generieren
        with st.status("🤖 LLM generiert Analyse...", expanded=True) as status:
            try:
                t0 = time.time()
                response = generate_once(base_url, model, full_prompt, timeout=timeout_s)
                dt = time.time() - t0
                
                status.update(label=f"✓ Analyse abgeschlossen in {dt:.2f}s", state="complete")
                
                # Ergebnis anzeigen
                st.divider()
                st.subheader("📊 LLM-Analyse Ergebnis")
                st.markdown(response)
                
                # Metadaten
                with st.expander("ℹ️ Analyse-Details"):
                    st.write(f"**Modell:** {model}")
                    st.write(f"**Vorhersagetyp:** {prediction_type}")
                    st.write(f"**Datenquelle:** {data_source}")
                    st.write(f"**Features:** {', '.join(feature_cols)}")
                    st.write(f"**Target:** {target_col}")
                    st.write(f"**Generierungszeit:** {dt:.2f}s")
                    st.write(f"**Sample-Größe:** {sample_size} Zeilen")
                
            except requests.HTTPError as http_err:
                st.error(f"❌ HTTP-Fehler: {http_err.response.status_code}")
                st.code(http_err.response.text)
            except Exception as e:
                st.error(f"❌ Fehler bei der Generierung: {e}")