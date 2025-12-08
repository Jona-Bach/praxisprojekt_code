from pathlib import Path
import json
import numpy as np
from backend.data_model import metrics_list
from collections import defaultdict
from typing import Union, Sequence, Dict, Any, List
import pandas as pd


# Datei-Pfad dieses Scripts
CURRENT_FILE = Path(__file__).resolve()
print("CURRENT_FILE:", CURRENT_FILE)

# Projekt-Root: drei Ebenen hoch: machine_learning → backend → src → praxisp_source
PROJECT_ROOT = CURRENT_FILE.parents[3]
print("PROJECT_ROOT:", PROJECT_ROOT)

# fmp_data liegt direkt unter dem Projekt-Root
FMP_DATA_DIR = PROJECT_ROOT / "fmp_data"
print("FMP_DATA_DIR:", FMP_DATA_DIR)


from pathlib import Path
import json
from collections import defaultdict
from typing import Union, Sequence, Dict, Any, List


def load_json_values(
    folder_path: Union[str, Path],
    fields: Union[str, Sequence[str]],
    pattern: str = "*.json",
) -> List[Dict[str, Any]]:
    """
    Liest alle JSON-Dateien ein und erzeugt *eine* Zeile pro (symbol, date, period),
    in die alle metriken aus verschiedenen Dateien (BalanceSheet, Ratios, key-metrics, ...)
    gemerged werden.

    - Mehrere Files pro Symbol/Datum werden zusammengeführt.
    - Wenn dieselbe Metrik in mehreren Files vorkommt:
        - später eingelesene Files überschreiben frühere (oder du änderst das).
    """
    folder = Path(folder_path)

    if isinstance(fields, str):
        fields = [fields]
    fields = list(fields)

    # key: (symbol, date, period)  ->  dict mit allen Features
    merged: dict[tuple, dict] = defaultdict(dict)

    for file in sorted(folder.glob(pattern)):
        # du kannst hier optional nach Typ filtern, z.B.
        # if "BalanceSheetStatement" in file.name: ...
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = json.load(f)
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON-Fehler in {file.name}: {e}")
            continue

        if isinstance(content, dict):
            objects = [content]
        elif isinstance(content, list):
            objects = content
        else:
            print(f"⚠️  Unerwartiger Typ in {file.name}: {type(content)}")
            continue

        for obj in objects:
            if not isinstance(obj, dict):
                continue

            symbol = obj.get("symbol")
            date = obj.get("date")
            period = obj.get("period")  # FY, Q1, etc.

            if symbol is None or date is None:
                # ohne Schlüssel kein sauberes Merging
                continue

            key = (symbol, date, period)

            row = merged[key]
            # Basisinfos einmal setzen
            row.setdefault("symbol", symbol)
            row.setdefault("date", date)
            row.setdefault("period", period)

            # alle gewünschten metriken ergänzen
            for field in fields:
                if field in obj and obj[field] is not None:
                    # policy: spätere Files dürfen überschreiben
                    row[field] = obj[field]

    # in eine Liste umwandeln
    return list(merged.values())


#rows = load_json_values(FMP_DATA_DIR, metrics_list,pattern="*.json")
TOTAL_SP_DIR = FMP_DATA_DIR / "total_sp_data"
rows = load_json_values(TOTAL_SP_DIR, metrics_list,pattern="*.json")
print("Anzahl Rows:", len(rows))
print(rows[:3])   # die ersten paar Einträge
print(len(rows))

df = pd.DataFrame(rows)
df = df.sort_values(["symbol", "date"])
df.to_excel("test_metric.xlsx")

print(df.head())