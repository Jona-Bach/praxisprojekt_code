import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np


# ===============================================
# 1. CSV einlesen
# ===============================================

df = pd.read_csv("datasets/prices.csv")  # <-- deine CSV hier
df["date"] = pd.to_datetime(df["date"])

# Nach Datum sortieren (wichtig!)
df = df.sort_values(["symbol", "date"]).reset_index(drop=True)

# ===============================================
# 2. Target erzeugen: Preis in Zukunft
#    Wir sagen hier: Preis 1 Tag in der Zukunft
# ===============================================

FUTURE_DAYS = 30  # <- kannst du z.B. 5, 10, 30 machen

df["future_close"] = df.groupby("symbol")["close"].shift(-FUTURE_DAYS)

# Zeilen löschen, wo future_close NaN ist (Ende der Serie)
df = df.dropna(subset=["future_close"])

# ===============================================
# 3. Features erzeugen (sehr einfach)
# ===============================================

# Lag-Features (Preis von gestern, vorgestern)
df["close_lag1"] = df.groupby("symbol")["close"].shift(1)
df["close_lag2"] = df.groupby("symbol")["close"].shift(2)

# Returns
df["return_1d"] = df["close"].pct_change()
df["return_lag1"] = df["close_lag1"].pct_change()

# Kleine Gleitende Durchschnitte
df["sma_3"] = df["close"].rolling(3).mean()
df["sma_5"] = df["close"].rolling(5).mean()

# Wieder Zeilen löschen, die NaN haben
df = df.dropna()

# ===============================================
# 4. Feature-Auswahl
# ===============================================

feature_cols = [
    "close", "open", "high", "low", "volume",
    "close_lag1", "close_lag2",
    "return_1d", "return_lag1",
    "sma_3", "sma_5",
]

X = df[feature_cols]
y = df["future_close"]

print("Features:", feature_cols)
print("Dataset-Shape:", X.shape)

# ===============================================
# 5. Train/Test Split
# ===============================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    shuffle=False  # Zeitreihendaten NICHT mischen!
)

# ===============================================
# 6. Modell trainieren
# ===============================================

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ===============================================
# 7. Evaluation
# ===============================================

preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
rmse = np.sqrt(mse)

print("\n=== Modell Ergebnisse ===")
print("RMSE:", rmse)
print("Erste Vorhersagen:")
print(pd.DataFrame({"actual": y_test.values[:10], "predicted": preds[:10]}))

# ===============================================
# 8. Modell für Vorhersagen benutzen
# ===============================================

df["prediction"] = np.nan
df.loc[X_test.index, "prediction"] = preds

df.to_csv("price_predictions.csv", index=False)
print("\nVorhersagen gespeichert in price_predictions.csv")