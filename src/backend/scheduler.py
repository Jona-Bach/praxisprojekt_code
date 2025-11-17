import time
from datetime import datetime
from src.backend.api_services.av_connect import fetch_alphavantage_raw, fetch_alphavantage_price_today
from src.backend.data_model import tickers


def load_data():
    today = datetime.today
    print(f"Loading data at: {today} ")

    for ticker in tickers:
        try:
            #fetch_alphavantage_raw(ticker)
            #fetch_alphavantage_price_today(ticker)
            print(f"{ticker} added to Database!")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(60)
    
    return f"Loaded data at: {today}"