from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix


# ======================================================
# 1. Dataset laden
# ======================================================

DATA_PATH = Path("datasets/training_dataset_processed.xlsx")  # ggf. Pfad anpassen
TARGET_COL = "target_next_report_up"

df = pd.read_excel(DATA_PATH)

print("Dataset geladen:", DATA_PATH)
print("Anzahl Zeilen:", len(df))
print("Spalten:")
print(df.columns.tolist())


# ======================================================
# 2. Spalten definieren (basierend auf deiner Liste)
# ======================================================

# Spalten, die NICHT als Features benutzt werden sollen
NON_FEATURE_COLS = [
    "date",
    "symbol_y",
    "symbol",
    "next_report_date",
    "timestamp_x",
    "timestamp_y",
    "close_t_plus_1",
    "return_next_report",
    TARGET_COL,
]

# Features: alles außer NON_FEATURE_COLS
feature_cols = [c for c in df.columns if c not in NON_FEATURE_COLS]

if TARGET_COL not in df.columns:
    raise ValueError(f"Target-Spalte '{TARGET_COL}' fehlt im DataFrame.")

print("\nVerwendete Feature-Spalten:")
print(feature_cols)
print("Target-Spalte:", TARGET_COL)


# ======================================================
# 3. Strings bereinigen & numerisch machen
# ======================================================

# Typische "Pseudo-NaN"-Strings zu echten NaN machen
NA_STRINGS = ["N/A", "n/a", "NA", "na", "-", "—", "null", "NULL", "Null", "None", ""]

df = df.replace(NA_STRINGS, pd.NA)

# Alle Feature-Spalten in numerisch konvertieren (Zahlen-Strings -> float)
for col in feature_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Target in Integer (0/1)
y = df[TARGET_COL].astype("Int64")

X = df[feature_cols].copy()

# Zeilen mit fehlendem Target oder komplett kaputten Features rauswerfen
mask_valid = y.notna() & X.notna().any(axis=1)
X = X[mask_valid]
y = y[mask_valid].astype(int)

print("\nNach Bereinigung:")
print("X Shape:", X.shape)
print("y Shape:", y.shape)


# ======================================================
# 4. Train/Test-Split
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print("\nTrain/Test Shapes:")
print("X_train:", X_train.shape)
print("X_test :", X_test.shape)


# ======================================================
# 5. Pipeline: Skalierung + RandomForest
# ======================================================

pipe = Pipeline(
    steps=[
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            n_jobs=-1,
        )),
    ]
)

pipe.fit(X_train, y_train)


# ======================================================
# 6. Evaluation
# ======================================================

train_acc = pipe.score(X_train, y_train)
test_acc = pipe.score(X_test, y_test)

print("\n=== Modell-Performance ===")
print("Train Accuracy:", round(train_acc, 4))
print("Test  Accuracy:", round(test_acc, 4))

y_pred = pipe.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ======================================================
# 7. Optional: Modell speichern
# ======================================================

if False:  # auf True setzen, wenn du speichern willst
    import joblib
    joblib.dump(pipe, "next_report_up_rf_pipeline.pkl")
    print("\nModell-Pipeline gespeichert als 'next_report_up_rf_pipeline.pkl'")