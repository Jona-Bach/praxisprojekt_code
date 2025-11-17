 
import os
from dotenv import load_dotenv
import requests
import json
from ..data_model import tickers
import time
from ..database.db_functions import create_av_raw_entry
load_dotenv()

# Wie lange VOR jedem Request gewartet wird (in Sekunden)
ALPHAVANTAGE_BASE_SLEEP = 20  # z.B. 20 Sekunden

# Wie lange gewartet wird, wenn ein "Note" (Rate Limit) kommt
ALPHAVANTAGE_LIMIT_SLEEP = 75  # z.B. 75 Sekunden


symbol = "AAPL"

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("API_KEY_AV")


def av_request(params, sleep_before: float = ALPHAVANTAGE_BASE_SLEEP):
    """Hilfsfunktion: API-Aufruf mit bewusst langer Wartezeit."""
    params["apikey"] = API_KEY

    # Basis-Wartezeit vor jedem Request
    if sleep_before and sleep_before > 0:
        time.sleep(sleep_before)

    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        data = response.json()

        # AlphaVantage Rate-Limit-Hinweis
        if "Note" in data:
            print("⚠ AlphaVantage Limit-Hinweis erhalten:")
            print(data["Note"])
            print(f"⏳ Warte nun {ALPHAVANTAGE_LIMIT_SLEEP} Sekunden und versuche es erneut …")
            time.sleep(ALPHAVANTAGE_LIMIT_SLEEP)
            return av_request(params, sleep_before=0)  # beim Retry nicht nochmal Basis-Sleep

        if "Error Message" in data:
            print("❌ AlphaVantage Fehler: ", data["Error Message"])
            return None

        return data

    except Exception as e:
        print("❌ Request error:", e)
        return None
    
overview = av_request({"function": "OVERVIEW", "symbol": symbol})

payout_ratio=(overview.get("PayoutRatio"))

cashflow = av_request({"function": "CASH_FLOW", "symbol": symbol}) or {}
cf = cashflow.get("annualReports", [{}])[0] if "annualReports" in cashflow else {}

balance = av_request({"function": "BALANCE_SHEET", "symbol": symbol}) or {}
bs = balance.get("annualReports", [{}])[0] if "annualReports" in balance else {}

income = av_request({"function": "INCOME_STATEMENT", "symbol": symbol}) or {}
inc = income.get("annualReports", [{}])[0] if "annualReports" in income else {}

print(cf)

