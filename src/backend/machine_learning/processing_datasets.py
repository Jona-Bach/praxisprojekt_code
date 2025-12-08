#df.to_csv("alle_preise.csv", index=False)
import pandas as pd

# ============================
# 1. Excel einlesen
# ============================

INPUT_FILE = "datasets/training_dataset_processed.xlsx"            # <- anpassen falls nötig
OUTPUT_FILE = "training_dataset_cleaned.xlsx"   # <- Ausgabe

df = pd.read_excel(INPUT_FILE)

print("Originale Anzahl Zeilen:", len(df))

# ============================
# 2. Filtern
#    -> lösche Zeilen, in denen
#       return_next_report == 0
#       und target_next_report_up == 0
# ============================

mask_bad = (df["return_next_report"] == 0) & (df["target_next_report_up"] == 0)

df_clean = df[~mask_bad].copy()   # nur Zeilen behalten, die NICHT bad sind

print("Entfernte Zeilen:", mask_bad.sum())
print("Neue Anzahl Zeilen:", len(df_clean))

# ============================
# 3. Neue Excel-Datei speichern
# ============================

df_clean.to_excel(OUTPUT_FILE, index=False)

print(f"Bereinigtes Dataset gespeichert als: {OUTPUT_FILE}")