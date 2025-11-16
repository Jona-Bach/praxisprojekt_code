import os
from dotenv import load_dotenv
import requests
import json
from ..data_model import tickers
import time
from ..database.db_functions import create_av_raw_entry
load_dotenv()

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = os.getenv("API_KEY_AV")

# Wie lange VOR jedem Request gewartet wird (in Sekunden)
ALPHAVANTAGE_BASE_SLEEP = 20  # z.B. 20 Sekunden

# Wie lange gewartet wird, wenn ein "Note" (Rate Limit) kommt
ALPHAVANTAGE_LIMIT_SLEEP = 75  # z.B. 75 Sekunden

symbol = tickers[0]

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
    
def fetch_alphavantage_raw(symbol: str):
    """Holt alle Rohdaten für einen Ticker von AlphaVantage mit großzügigen Wartezeiten."""
    
    print(f"\n📡 Lade AlphaVantage Rohdaten für {symbol} …")

    # --- Overview ---
    overview = av_request({"function": "OVERVIEW", "symbol": symbol}) or {}

    # --- Cash Flow ---
    cashflow = av_request({"function": "CASH_FLOW", "symbol": symbol}) or {}
    cf = cashflow.get("annualReports", [{}])[0] if "annualReports" in cashflow else {}

    # --- Balance Sheet ---
    balance = av_request({"function": "BALANCE_SHEET", "symbol": symbol}) or {}
    bs = balance.get("annualReports", [{}])[0] if "annualReports" in balance else {}

    # --- Income Statement ---
    income = av_request({"function": "INCOME_STATEMENT", "symbol": symbol}) or {}
    inc = income.get("annualReports", [{}])[0] if "annualReports" in income else {}

    def num(x):
        try:
            return float(x)
        except:
            return None

    entry = create_av_raw_entry(
        symbol=symbol,

        # --- DIRECT from OVERVIEW ---
        price_to_book=num(overview.get("PriceToBookRatio")),
        dividend_yield=num(overview.get("DividendYield")),
        payout_ratio=num(overview.get("PayoutRatio")),
        roe_ttm=num(overview.get("ReturnOnEquityTTM")),
        roa_ttm=num(overview.get("ReturnOnAssetsTTM")),
        profit_margin=num(overview.get("ProfitMargin")),
        revenue_growth_qoq=num(overview.get("QuarterlyRevenueGrowthYOY")),
        earnings_growth_qoq=num(overview.get("QuarterlyEarningsGrowthYOY")),
        asset_turnover=num(overview.get("AssetTurnover")),
        equity_ratio=num(overview.get("equityRatio")),
        debt_ratio=num(overview.get("debtRatio")),
        pe_ratio=num(overview.get("PERatio")),
        price_to_sales=num(overview.get("PriceToSalesRatioTTM")),
        peg_ratio=num(overview.get("PEGRatio")),
        ev_to_ebitda=num(overview.get("EVToEBITDA")),
        beta=num(overview.get("Beta")),
        eps=num(overview.get("EPS")),
        free_cash_flow=num(overview.get("FreeCashFlow")),

        # --- CASHFLOW ---
        operating_cashflow=num(cf.get("operatingCashflow")),
        capex=num(cf.get("capitalExpenditures")),

        # --- BALANCE SHEET ---
        total_assets=num(bs.get("totalAssets")),
        total_liabilities=num(bs.get("totalLiabilities")),
        total_equity=num(bs.get("totalShareholderEquity")),
        cash=num(bs.get("cashAndCashEquivalentsAtCarryingValue")),
        current_assets=num(bs.get("totalCurrentAssets")),
        current_liabilities=num(bs.get("totalCurrentLiabilities")),

        # --- INCOME STATEMENT ---
        revenue=num(inc.get("totalRevenue")),
        gross_profit=num(inc.get("grossProfit")),
        operating_income=num(inc.get("operatingIncome")),
        ebitda=num(inc.get("ebitda")),
        net_income=num(inc.get("netIncome")),
    )

    print(f"✔ Rohdaten für {symbol} gespeichert.")
    return entry