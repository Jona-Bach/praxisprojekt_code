kpi_list = [
    "Kurs-Buchwert-Verhältnis (KBV)",
    "Kurs-Cashflow-Verhältnis (KCV)",
    "Dividendenrendite",
    "Ausschüttungsquote (Payout Ratio)",
    "Eigenkapitalrendite (ROE)",
    "Gesamtkapitalrendite (ROA)",
    "Return on Capital Employed (ROCE)",
    "Return on Invested Capital (ROIC)",
    "Bruttogewinnmarge",
    "EBIT-Marge",
    "EBITDA-Marge",
    "Nettogewinnmarge",
    "Umsatzwachstum",
    "Gewinnwachstum",
    "Kapitalumschlag",
    "Working Capital",
    "Cashflow-Marge",
    "Liquidität 1. Grades (Cash Ratio)",
    "Liquidität 2. Grades (Quick Ratio)",
    "Liquidität 3. Grades (Current Ratio)",
    "Eigenkapitalquote",
    "Fremdkapitalquote",
    "Dynamischer Verschuldungsgrad",
    "Zinsdeckungsgrad",
    "Anlagendeckungsgrad I",
    "Anlagendeckungsgrad II",
    "Kurs-Gewinn-Verhältnis (Wachstum) (KGV)",
    "Kurs-Umsatz-Verhältnis (KUV)",
    "PEG Ratio",
    "Free Cashflow",
    "Operativer Cashflow",
    "Gewinn je Aktie (EPS)",
    "Verschuldungsgrad",
    "EV/EBITDA",
    "Beta",
    "Graham-Number"
]

alpha_vantage_kpis = {
    "Kurs-Buchwert-Verhältnis (KBV)": "PriceToBookRatio",
    "Dividendenrendite": "DividendYield",
    "Ausschüttungsquote (Payout Ratio)": "PayoutRatio",
    "Eigenkapitalrendite (ROE)": "ReturnOnEquityTTM",
    "Gesamtkapitalrendite (ROA)": "ReturnOnAssetsTTM",
    "Nettogewinnmarge": "ProfitMargin",
    "Umsatzwachstum": "QuarterlyRevenueGrowthYOY",  # *4 für annualisiert
    "Gewinnwachstum": "QuarterlyEarningsGrowthYOY",  # *4 für annualisiert
    "Kapitalumschlag": "AssetTurnover",
    "Cashflow-Marge": "operating_cashflow_margin",   # operatingCashFlow / revenue (selbst berechnen)
    "Eigenkapitalquote": "equityRatio",
    "Fremdkapitalquote": "debtRatio",
    "Kurs-Gewinn-Verhältnis (Wachstum) (KGV)": "PERatio",
    "Kurs-Umsatz-Verhältnis (KUV)": "PriceToSalesRatioTTM",
    "PEG Ratio": "PEGRatio",
    "Free Cashflow": "freeCashFlow",                 # operatingCashFlow - capex
    "Operativer Cashflow": "operatingCashFlow",
    "Gewinn je Aktie (EPS)": "EPS",
    "EV/EBITDA": "EVToEBITDA",
    "Beta": "Beta"
}

initial_tickers = [
    "AAPL",   # Apple
    "MSFT",   # Microsoft
    "GOOGL",  # Alphabet (Google)
    "AMZN",   # Amazon
    "META",   # Meta Platforms
    "TSLA",   # Tesla
    "NVDA",   # Nvidia
    "JPM",    # JPMorgan Chase
    "V",      # Visa
    "NFLX"    # Netflix
]

TICKERS = [
    # USA – Mega Caps / Tech
    "AAPL", "MSFT", "GOOG", "GOOGL", "AMZN", "META", "NFLX", "TSLA", "NVDA",
    "AVGO", "ADBE", "INTC", "CSCO", "ORCL", "IBM", "AMD", "QCOM", "TXN",
    "CRM", "INTU", "SHOP", "UBER", "LYFT", "SNOW", "ABNB", "PYPL", "SQ",

    # USA – Consumer / Retail
    "WMT", "COST", "TGT", "HD", "LOW", "MCD", "SBUX", "NKE", "DIS", "KO",
    "PEP", "PG", "PM", "MO", "KHC", "MDLZ", "CL", "EL", "UL", "DEO",

    # USA – Finance
    "JPM", "BAC", "WFC", "C", "GS", "MS", "BLK", "AXP", "V", "MA", "SCHW",
    "BK", "USB", "PNC", "TFC",

    # USA – Healthcare / Pharma / Biotech
    "JNJ", "PFE", "MRNA", "BMY", "ABBV", "LLY", "AZN", "GILD", "AMGN", "REGN",
    "UNH", "HUM", "CI", "ISRG", "DHR", "TMO", "SYK", "MDT", "BSX",

    # USA – Energy / Materials / Industrials
    "XOM", "CVX", "COP", "SLB", "EOG", "PSX", "MPC", "VLO",
    "CAT", "DE", "GE", "HON", "BA", "LMT", "NOC", "RTX", "GD",
    "LIN", "APD", "SHW", "DD", "FCX", "NEM",

    # USA – Communication / Media
    "T", "VZ", "TMUS", "CHTR", "CMCSA", "DIS", "PARA", "WBD",

    # USA – REITs
    "PLD", "AMT", "CCI", "O", "SPG", "DLR", "EQIX",

    # USA – ETFs (falls du die auch willst)
    "SPY", "IVV", "VOO", "QQQ", "IWM", "DIA", "XLK", "XLF", "XLV", "XLE",
    "XLY", "XLP", "XLI", "XLB", "XLU", "IEMG", "EEM",

    # Deutschland – Blue Chips (XETRA)
    "SAP", "SIE", "DTE", "ALV", "BAS", "BAYN", "BMW", "MBG", "VOW3", "VNA",
    "MUV2", "LIN", "HEN3", "DPW", "FRE", "RWE", "EOAN", "IFX", "DBK", "HEI",

    # Deutschland – weitere bekannte Werte
    "FME", "BEI", "ZAL", "ADS", "MTX", "EVK", "HNR1", "PUM", "1COV",

    # Europa – Großbritannien
    "AZN.L", "BP.L", "SHEL.L", "HSBA.L", "ULVR.L", "GSK.L", "RIO.L",
    "BATS.L", "DGE.L", "LLOY.L", "BARC.L", "VOD.L",

    # Europa – Frankreich
    "MC.PA", "OR.PA", "AIR.PA", "BN.PA", "DG.PA", "SU.PA", "SAN.PA",
    "AI.PA", "BNP.PA", "GLE.PA",

    # Europa – Schweiz
    "NESN.SW", "ROG.SW", "NOVN.SW", "ZURN.SW", "CSGN.SW", "UBSG.SW",

    # Europa – Nordics
    "NOKIA.HE", "ERIC-B.ST", "VOLV-B.ST", "ATCO-A.ST", "TELIA.ST",

    # Kanada
    "SHOP.TO", "RY.TO", "TD.TO", "ENB.TO", "SU.TO", "BNS.TO", "BMO.TO",

    # Asien – Japan
    "7203.T",  # Toyota
    "6758.T",  # Sony
    "9984.T",  # SoftBank
    "9432.T",  # NTT
    "8306.T",  # MUFG
    "7974.T",  # Nintendo

    # Asien – China / Hongkong (ADR/US + HK)
    "BABA", "BIDU", "JD", "TCEHY", "PDD", "NTES",
    "0700.HK", "0939.HK", "1398.HK", "2318.HK",

    # Indien
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "SBIN.NS", "ICICIBANK.NS",

    # Noch ein paar bekannte Tech-/Growth-Namen
    "PLTR", "CRWD", "ZS", "NET", "OKTA", "TWLO", "DOCU",
    "ROKU", "ETSY", "MELI", "SE", "ZM", "ROKU", "DDOG", "TEAM",
]