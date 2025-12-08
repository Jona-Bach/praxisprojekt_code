from pathlib import Path
from collections import defaultdict
from typing import Union, Sequence, Dict, Any, List
import json
import pandas as pd
from backend.database.db_functions import get_yf_price_history_ml
from backend.data_model import metrics_list

# Datei-Pfad dieses Scripts
CURRENT_FILE = Path(__file__).resolve()
print("CURRENT_FILE:", CURRENT_FILE)

# Projekt-Root: drei Ebenen hoch: machine_learning → backend → src → praxisp_source
PROJECT_ROOT = CURRENT_FILE.parents[3]
print("PROJECT_ROOT:", PROJECT_ROOT)

# fmp_data liegt direkt unter dem Projekt-Root
FMP_DATA_DIR = PROJECT_ROOT / "fmp_data"
print("FMP_DATA_DIR:", FMP_DATA_DIR)

TOTAL_SP_DIR = FMP_DATA_DIR / "total_sp_data"

from pathlib import Path
from collections import defaultdict
from typing import Union, Sequence, Dict, Any, List
import json
import pandas as pd
from backend.database.db_functions import get_yf_price_history
from backend.data_model import metrics_list


def build_ml_dataset(
    fundamentals_dir: Union[str, Path],
    metrics_list: Sequence[str],
    pattern: str = "*.json",
) -> pd.DataFrame:
    """
    1) Lädt Fundamental-JSONs und merged sie zu einer Zeile pro (symbol, date, period)
    2) Holt Price-Historie je Symbol aus der DB
    3) Matched für jeden Report den Kurs zum Report (close_t) und zum nächsten Report (close_t_plus_1)
    4) Berechnet return_next_report und target_next_report_up (1 = Kurs steigt bis zum nächsten Report)
    """

    fundamentals_dir = Path(fundamentals_dir)

    # -----------------------------
    # 1) Fundamentals laden & mergen
    # -----------------------------
    folder = fundamentals_dir
    fields = list(metrics_list)

    merged: Dict[tuple, Dict[str, Any]] = defaultdict(dict)

    for file in sorted(folder.glob(pattern)):
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
                continue

            key = (symbol, date, period)
            row = merged[key]

            row.setdefault("symbol", symbol)
            row.setdefault("date", date)
            row.setdefault("period", period)

            for field in fields:
                if field in obj and obj[field] is not None:
                    row[field] = obj[field]

    rows: List[Dict[str, Any]] = list(merged.values())
    if not rows:
        print("⚠️ Keine Fundamental-Daten gefunden.")
        return pd.DataFrame()

    fund_df = pd.DataFrame(rows)
    if "symbol" not in fund_df.columns or "date" not in fund_df.columns:
        raise ValueError("Fundamental-Daten müssen 'symbol' und 'date' enthalten.")

    fund_df["date"] = pd.to_datetime(fund_df["date"])
    fund_df = fund_df.sort_values(["symbol", "date"]).reset_index(drop=True)

    # ---------------------------------
    # 2) Pro Symbol: Preise holen & mergen
    # ---------------------------------
    all_symbol_results: List[pd.DataFrame] = []
    symbols = fund_df["symbol"].dropna().unique()

    for sym in symbols:
        df_fund_sym = fund_df[fund_df["symbol"] == sym].copy()
        df_fund_sym = df_fund_sym.sort_values("date")

        df_price_sym = get_yf_price_history_ml(sym)
        if df_price_sym is None or df_price_sym.empty:
            print(f"⚠️ Keine Preis-Daten für Symbol {sym} gefunden.")
            continue

        if "date" not in df_price_sym.columns or "close" not in df_price_sym.columns:
            raise ValueError("Preis-Daten müssen 'date' und 'close' enthalten.")

        df_price_sym = df_price_sym.copy()
        df_price_sym["date"] = pd.to_datetime(df_price_sym["date"])
        df_price_sym = df_price_sym.sort_values("date")

        # 3a) close_t: Kurs zum/ nach Report-Datum
        merged_t = pd.merge_asof(
            df_fund_sym.sort_values("date"),
            df_price_sym.sort_values("date"),
            left_on="date",
            right_on="date",
            direction="forward",   # nächster Handelstag nach Report
        )
        merged_t = merged_t.rename(columns={"close": "close_t"})

        # 4) nächstes Report-Datum innerhalb desselben Symbols
        merged_t["next_report_date"] = merged_t["date"].shift(-1)

        # 5) close_t_plus_1: Kurs zum nächsten Report-Datum
        tmp = merged_t.dropna(subset=["next_report_date"]).copy()
        if tmp.empty:
            continue

        prices_next = df_price_sym.rename(columns={"date": "price_date"})
        merged_next = pd.merge_asof(
            tmp.sort_values("next_report_date"),
            prices_next.sort_values("price_date"),
            left_on="next_report_date",
            right_on="price_date",
            direction="forward",
        )
        merged_next = merged_next.rename(columns={"close": "close_t_plus_1"})
        merged_next = merged_next.drop(columns=["price_date"])

        # 6) Return & Target
        merged_next = merged_next.dropna(subset=["close_t", "close_t_plus_1"]).copy()
        if merged_next.empty:
            continue

        merged_next["return_next_report"] = (
            merged_next["close_t_plus_1"] / merged_next["close_t"] - 1.0
        )
        merged_next["target_next_report_up"] = (
            merged_next["return_next_report"] > 0
        ).astype(int)

        all_symbol_results.append(merged_next)

    if not all_symbol_results:
        print("⚠️ Kein Symbol hatte gleichzeitig Fundamentals und Prices mit genügend Daten.")
        return pd.DataFrame()

    df_final = pd.concat(all_symbol_results, ignore_index=True)
    df_final = df_final.sort_values(["symbol", "date"]).reset_index(drop=True)

    return df_final

dataset = build_ml_dataset(
    fundamentals_dir=TOTAL_SP_DIR,
    metrics_list=metrics_list,
    pattern="*.json",
)

print(dataset.head())
dataset.to_excel("training_dataset.xlsx", index=False)
