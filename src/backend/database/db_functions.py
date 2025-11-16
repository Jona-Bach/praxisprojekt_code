from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, DateTime, inspect
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
import os

def create_av_alchemy_db(folder_name, db_name):
    current_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(current_dir, "../../.."))
    data_folder = os.path.join(project_root, folder_name)
    os.makedirs(data_folder, exist_ok=True)

    db_path = os.path.join(data_folder, f"{db_name}.db")
    engine = create_engine(f"sqlite:///{db_path}", echo=False)
    Base = declarative_base()
    Session = sessionmaker(bind = engine)
    session = Session()

    return engine, Base, session, db_path

engine, Base, session, dbpath = create_av_alchemy_db("data", "av_raw")


class AV_RAW(Base):
    __tablename__ = "alphavantage_raw_kpi"

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, index=True)

    price_to_book = Column(Float)              # KBV (direct)
    dividend_yield = Column(Float)             # Dividendenrendite (direct)
    payout_ratio = Column(Float)               # Ausschüttungsquote (direct)
    roe_ttm = Column(Float)                    # ROE (direct)
    roa_ttm = Column(Float)                    # ROA (direct)
    profit_margin = Column(Float)              # Nettogewinnmarge (direct)
    revenue_growth_qoq = Column(Float)         # Umsatzwachstum (direct)
    earnings_growth_qoq = Column(Float)        # Gewinnwachstum (direct)
    asset_turnover = Column(Float)             # Kapitalumschlag (direct)
    equity_ratio = Column(Float)               # Eigenkapitalquote (direct)
    debt_ratio = Column(Float)                 # Fremdkapitalquote (direct)
    pe_ratio = Column(Float)                   # KGV (direct)
    price_to_sales = Column(Float)             # KUV (direct)
    peg_ratio = Column(Float)                  # PEG Ratio (direct)
    ev_to_ebitda = Column(Float)               # EV/EBITDA (direct)
    beta = Column(Float)                       # Beta (direct)
    eps = Column(Float)                        # EPS (direct)
    free_cash_flow = Column(Float)             # Free Cashflow (direct)

    # ---- Cash Flow (Direct) ----
    operating_cashflow = Column(Float)         # Operativer Cashflow (direct)
    capex = Column(Float)                      # CAPEX (direct)

    # ---- Balance Sheet (Direct) ----
    total_assets = Column(Float)               # Total Assets (direct)
    total_liabilities = Column(Float)          # Total Liabilities (direct)
    total_equity = Column(Float)               # Total Equity (direct)
    cash = Column(Float)                       # Cash (direct)
    current_assets = Column(Float)             # Current Assets (direct)
    current_liabilities = Column(Float)        # Current Liabilities (direct)

    # ---- Income Statement (Direct) ----
    revenue = Column(Float)                    # Revenue (direct)
    gross_profit = Column(Float)               # Gross Profit (direct)
    operating_income = Column(Float)           # Operating Income (direct)
    ebitda = Column(Float)                     # EBITDA (direct)
    net_income = Column(Float)                 # Net Income (direct)

    # ---- Calculated KPIs ----
    kcv = Column(Float)                        # Kurs-Cashflow-Verhältnis (calc)
    roce = Column(Float)                       # ROCE (calc)
    roic = Column(Float)                       # ROIC (calc)
    gross_margin = Column(Float)               # Bruttogewinnmarge (calc)
    ebit_margin = Column(Float)                # EBIT-Marge (calc)
    ebitda_margin = Column(Float)              # EBITDA-Marge (calc)
    working_capital = Column(Float)            # Working Capital (calc)
    cashflow_margin = Column(Float)            # Cashflow-Marge (calc)
    cash_ratio = Column(Float)                 # Liquidität 1. Grades (calc)
    quick_ratio = Column(Float)                # Liquidität 2. Grades (calc)
    current_ratio = Column(Float)              # Liquidität 3. Grades (calc)
    leverage_ratio = Column(Float)             # Verschuldungsgrad (calc)
    graham_number = Column(Float)              # Graham-Number (calc)

    # ---- NOT AVAILABLE KPIs ----
    dyn_verschuldungsgrad = Column(Float)      # Dynamischer Verschuldungsgrad (na)
    zinsdeckungsgrad = Column(Float)           # Zinsdeckungsgrad (na)
    anlagendeckungsgrad_1 = Column(Float)      # Anlagendeckungsgrad I (na)
    anlagendeckungsgrad_2 = Column(Float)      # Anlagendeckungsgrad II (na)

    # ---- Metadata ----
    timestamp = Column(DateTime(timezone=True), server_default=func.now())


# -------------------------------------------------
# Prüfen, ob die Tabelle existiert → falls nicht, erstellen
# -------------------------------------------------
inspector = inspect(engine)

if "alphavantage_raw_kpi" not in inspector.get_table_names():
    Base.metadata.create_all(engine)
    print("✔ Tabelle erstellt.")
else:
    print("✔ Tabelle existiert bereits – kein Erstellen nötig.")


# -------------------------------------------------
# Funktion zum Erstellen eines neuen Eintrags
# -------------------------------------------------
def create_av_raw_entry(
    symbol: str,
    price_to_book=None,
    dividend_yield=None,
    payout_ratio=None,
    roe_ttm=None,
    roa_ttm=None,
    profit_margin=None,
    revenue_growth_qoq=None,
    earnings_growth_qoq=None,
    asset_turnover=None,
    equity_ratio=None,
    debt_ratio=None,
    pe_ratio=None,
    price_to_sales=None,
    peg_ratio=None,
    ev_to_ebitda=None,
    beta=None,
    eps=None,
    free_cash_flow=None,

    operating_cashflow=None,
    capex=None,

    total_assets=None,
    total_liabilities=None,
    total_equity=None,
    cash=None,
    current_assets=None,
    current_liabilities=None,

    revenue=None,
    gross_profit=None,
    operating_income=None,
    ebitda=None,
    net_income=None,

    # calculated
    kcv=None,
    roce=None,
    roic=None,
    gross_margin=None,
    ebit_margin=None,
    ebitda_margin=None,
    working_capital=None,
    cashflow_margin=None,
    cash_ratio=None,
    quick_ratio=None,
    current_ratio=None,
    leverage_ratio=None,
    graham_number=None,

    # not available
    dyn_verschuldungsgrad=None,
    zinsdeckungsgrad=None,
    anlagendeckungsgrad_1=None,
    anlagendeckungsgrad_2=None,
):
    """Erstellt einen vollständigen AlphaVantage-DB-Eintrag."""

    entry = AV_RAW(
        symbol=symbol,

        price_to_book=price_to_book,
        dividend_yield=dividend_yield,
        payout_ratio=payout_ratio,
        roe_ttm=roe_ttm,
        roa_ttm=roa_ttm,
        profit_margin=profit_margin,
        revenue_growth_qoq=revenue_growth_qoq,
        earnings_growth_qoq=earnings_growth_qoq,
        asset_turnover=asset_turnover,
        equity_ratio=equity_ratio,
        debt_ratio=debt_ratio,
        pe_ratio=pe_ratio,
        price_to_sales=price_to_sales,
        peg_ratio=peg_ratio,
        ev_to_ebitda=ev_to_ebitda,
        beta=beta,
        eps=eps,
        free_cash_flow=free_cash_flow,

        operating_cashflow=operating_cashflow,
        capex=capex,

        total_assets=total_assets,
        total_liabilities=total_liabilities,
        total_equity=total_equity,
        cash=cash,
        current_assets=current_assets,
        current_liabilities=current_liabilities,

        revenue=revenue,
        gross_profit=gross_profit,
        operating_income=operating_income,
        ebitda=ebitda,
        net_income=net_income,

        # calculated
        kcv=kcv,
        roce=roce,
        roic=roic,
        gross_margin=gross_margin,
        ebit_margin=ebit_margin,
        ebitda_margin=ebitda_margin,
        working_capital=working_capital,
        cashflow_margin=cashflow_margin,
        cash_ratio=cash_ratio,
        quick_ratio=quick_ratio,
        current_ratio=current_ratio,
        leverage_ratio=leverage_ratio,
        graham_number=graham_number,

        # not available
        dyn_verschuldungsgrad=dyn_verschuldungsgrad,
        zinsdeckungsgrad=zinsdeckungsgrad,
        anlagendeckungsgrad_1=anlagendeckungsgrad_1,
        anlagendeckungsgrad_2=anlagendeckungsgrad_2,
    )

    try:
        session.add(entry)
        session.commit()
    except IntegrityError:
        session.rollback()
        print(f"ERROR")

    print(f"✔ Neuer Eintrag für {symbol} gespeichert.")
    return entry