import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path
from datetime import datetime
from backend.data_model import TICKERS
from backend.scheduler import load_data, load_initial_data
from backend.database.db_functions import get_table, get_table_names, get_symbols_from_table, get_unique_table, get_yf_company_info
from backend.data_processing.alphavantage_processed import get_processed_table, process_alphavantage_raw_db, get_processed_entries_by_symbol
from backend.database.users_database import import_file_as_table, get_user_table, list_user_tables
import openpyxl
# Ordner der aktuellen Datei (z.B. app.py)
BASE_DIR = Path(__file__).resolve().parent

# Pfad zur PNG
img_path_fsbar = BASE_DIR.parent / "assets" / "finsightbar.png"
#__________________________Header____________________________

st.set_page_config(page_title="Data", page_icon="🔍")
#__________________________Global Dekleration_____________________________

tab1, tab2 = st.tabs(["Analysis","Data Settings"])
database_path_yf = "data/yfinance.db"

# --------------------------------------
# Card-Style CSS (einmal am Anfang der App)
# --------------------------------------
CARD_STYLE = """
<style>
.info-card {
    background-color: #1f2937;
    padding: 1rem 1.2rem;
    border-radius: 0.8rem;
    border: 1px solid #374151;
    margin-bottom: 1rem;
}
.info-title {
    font-size: 0.75rem;
    color: #9ca3af;
    margin-bottom: 0.3rem;
}
.info-value {
    font-size: 1.0rem;
    font-weight: 600;
    color: #f9fafb;
    overflow-wrap: break-word;
}
</style>
"""
st.markdown(CARD_STYLE, unsafe_allow_html=True)


def info_card(title, value):
    value = value if value else "—"
    return f"""
    <div class="info-card">
        <div class="info-title">{title}</div>
        <div class="info-value">{value}</div>
    </div>
    """

def format_number(value):
    if value is None:
        return "—"

    # String → Float umwandeln
    if isinstance(value, str):
        value = value.replace(".", "").replace(",", "")
        try:
            value = float(value)
        except:
            return "—"

    abs_val = abs(value)

    # Billiarden (10^15)
    if abs_val >= 1_000_000_000_000_000:
        return f"{value / 1_000_000_000_000_000:.2f} Bil"

    # Billionen (10^12)
    elif abs_val >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f} Bio."

    # Milliarden (10^9)
    elif abs_val >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f} Mrd."

    # Millionen (10^6)
    elif abs_val >= 1_000_000:
        return f"{value / 1_000_000:.2f} Mio."

    # Tausend
    elif abs_val >= 1_000:
        return f"{value / 1_000:.2f} Tsd."

    # Normale Zahl
    else:
        return f"{value:.2f}"

def format_number_en(value):
    """
    Format number using English short scale:
    - T (Trillion)
    - B (Billion)
    - M (Million)
    - K (Thousand)

    Always 2 decimals, automatically converts strings, adds $ sign.
    """
    if value is None:
        return "—"

    # Convert strings to float
    if isinstance(value, str):
        try:
            value = float(value.replace(",", "").replace(" ", ""))
        except:
            return "—"

    abs_val = abs(value)

    # Trillion (10^12)
    if abs_val >= 1_000_000_000_000:
        return f"$ {value / 1_000_000_000_000:.2f} Trillion"

    # Billion (10^9)
    elif abs_val >= 1_000_000_000:
        return f"$ {value / 1_000_000_000:.2f} Billion"

    # Million (10^6)
    elif abs_val >= 1_000_000:
        return f"$ {value / 1_000_000:.2f} Million"

    # Thousand (10^3)
    elif abs_val >= 1_000:
        return f"$ {value / 1_000:.2f} Thousand"

    # Normal number
    else:
        return f"$ {value:.2f}"


#__________________________SIDEBAR___________________________
st.sidebar.subheader("Data")
#st.sidebar.image(str(img_path_fsbar))
st.sidebar.divider()

if "load_data_time" in st.session_state:
    loaded_data_ts = st.session_state["load_data_time"]
else:
    st.session_state["load_data_time"] = "NOT NOW"
    loaded_data_ts = st.session_state["load_data_time"]


st.sidebar.subheader("Options:")

st.sidebar.info(f"Last data update: {loaded_data_ts}")
if st.sidebar.button("Update Data"):
    with st.spinner("Updating data (this might take a while...)"):
        database_path = "data/alphavantage.db"
        av_raw_data_symbols = get_symbols_from_table(database_path=database_path, table_name="alphavantage_raw_kpi")
        av_pricing_symbols = get_symbols_from_table(database_path=database_path, table_name="alphavantage_daily_pricing")
        all_tickers_to_update = av_raw_data_symbols + av_pricing_symbols
        unique_list = sorted(list(set(all_tickers_to_update)))
        answer = load_data(unique_list)
        st.success(answer)
    updated_time = datetime.now().replace(microsecond=0)
    st.success(f"Updated Data at:{updated_time}!")

if st.sidebar.button("Update Processed Data"):
    process_alphavantage_raw_db()
    st.success("Updated Processed Data!")

t_choice = st.sidebar.multiselect(
    "Choose Ticker",
    options=sorted(TICKERS))

st.session_state["chosen_tickers"] = t_choice

if st.sidebar.button("Download Ticker Data"):
    with st.spinner("Downloading data (this might take a while...)"):
        answer = load_data(t_choice)
        st.success(answer)
    st.success("Download Complete!")



st.sidebar.divider()


st.sidebar.subheader("Create your own Database")

# 1. Datei-Upload
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx", "xls"],
)

# 2. Tabellenname
default_table_name = ""
if uploaded_file is not None:
    # Vorschlag: Dateiname ohne Endung
    default_table_name = uploaded_file.name.rsplit(".", 1)[0]

table_name = st.sidebar.text_input(
    "Table name in database",
    value=default_table_name,
    help="Name der Tabelle in deiner users_database",
)

# 3. Verhalten bei vorhandener Tabelle
if_exists_option = st.sidebar.selectbox(
    "If table exists",
    options=["fail", "replace", "append"],
    index=1,  # default: replace
    help=(
        "'fail' = Fehler, wenn Tabelle existiert\n"
        "'replace' = Tabelle löschen + neu anlegen\n"
        "'append' = Zeilen an bestehende Tabelle anhängen"
    ),
)

# 4. Import-Button
if st.sidebar.button("Import file into database"):
    if uploaded_file is None:
        st.sidebar.error("Please upload a file first.")
    elif not table_name:
        st.sidebar.error("Please enter a table name.")
    else:
        try:
            df_preview = import_file_as_table(
                file_obj=uploaded_file,
                filename=uploaded_file.name,
                table_name=table_name,
                if_exists=if_exists_option,
            )
            st.success(f"✅ Table '{table_name}' successfully saved in users_database.")
            st.write("### Preview of imported data")
            st.dataframe(df_preview.head(), hide_index=True)
        except Exception as e:
            st.error(f"❌ Error while importing: {e}")













#___________________________Data Tab_________________________________


with tab1:

    st.header("Stock Analysis")
    st.divider()

    with st.container():
        st.subheader("Basic Analysis")
        ticker_to_analyze = st.selectbox(
            label="Choose Stock to Analyze",
            options=TICKERS
        )
        stock_info = get_yf_company_info(ticker_to_analyze)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(info_card("Symbol", stock_info["symbol"].iloc[0]), unsafe_allow_html=True)
        with col2:
            st.markdown(info_card("Short Name", stock_info["shortName"].iloc[0]), unsafe_allow_html=True)
        with col3:
            st.markdown(info_card("Country", stock_info["country"].iloc[0]), unsafe_allow_html=True)
        
        col4, col5, col6 = st.columns(3)
        with col4:
            st.markdown(info_card("Sector", stock_info["sector"].iloc[0]), unsafe_allow_html=True)
        with col5:
            st.markdown(info_card("Industry", stock_info["industry"].iloc[0]), unsafe_allow_html=True)
        with col6:
            st.markdown(info_card("Website", stock_info["website"].iloc[0]), unsafe_allow_html=True)

        st.markdown(info_card("Business Summary", stock_info["longBusinessSummary"].iloc[0]), unsafe_allow_html=True)
        st.divider()

        col7, col8, col9 = st.columns(3)

        try:
            # Versuche vorhandene Daten zu lesen
            up_to_date_av_entries = get_processed_entries_by_symbol(
                "alphavantage_processed_kpi", ticker_to_analyze
            )

            # Falls leer → Daten müssen nachgeladen werden
            if up_to_date_av_entries is None or len(up_to_date_av_entries) == 0:
                raise ValueError("Keine Daten vorhanden")

        except Exception:
            # Daten laden
            with st.spinner("Loading current data.."):
                load_data([ticker_to_analyze])

                # Erneut abrufen
                up_to_date_av_entries = get_processed_entries_by_symbol(
                    "alphavantage_processed_kpi", ticker_to_analyze
                )

        market_cap_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["market_capitalization"].iloc[0]
        market_cap = format_number(market_cap_str)
        pre_ratio_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["pe_ratio"].iloc[0]
        pe_ratio = format_number(pre_ratio_str)
        price_to_book_ratio_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["price_to_book_ratio"].iloc[0]
        ptbr = format_number(price_to_book_ratio_str)
        
        col7.metric("Market Capitalization", market_cap)
        col8.metric("PE-Ratio", pe_ratio)
        col9.metric("Price/Book", price_to_book_ratio_str)

        col10, col11, col12 = st.columns(3)

        roe_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["return_on_equity_ttm"].iloc[0]
        roe = format_number(roe_str)
        profit_margin_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["profit_margin_raw"].iloc[0]
        profit_margin = format_number(profit_margin_str)
        beta_str = up_to_date_av_entries.sort_values("timestamp", ascending=False)["beta_raw"].iloc[0]
        beta = format_number(beta_str)

             
        col10.metric("ROE", roe)
        col11.metric("Profit-Margin", f"{profit_margin}€")
        col12.metric("Beta", beta)






with tab2:
    st.title("Database Viewer")

    st.markdown("Explore all Alphavantage tables as well as your own uploaded datasets.")

    # ---------------------------------------------------------------
    # SECTION 1: Alphavantage RAW data
    # ---------------------------------------------------------------
    st.subheader("Alphavantage Raw KPI Data")
    try:
        df_raw_kpi = get_table("alphavantage_raw_kpi")
        st.dataframe(df_raw_kpi, hide_index=True, width="stretch")
    except Exception as e:
        st.error(f"Could not load raw KPI data: {e}")

    st.subheader("Alphavantage Raw Pricing Data")
    try:
        df_raw_pricing = get_table("alphavantage_daily_pricing")
        st.dataframe(df_raw_pricing, hide_index=True, width="stretch")
    except Exception as e:
        st.error(f"Could not load raw pricing data: {e}")

    st.divider()

    # ---------------------------------------------------------------
    # SECTION 2: Alphavantage Processed data
    # ---------------------------------------------------------------
    st.subheader("Processed KPI Data")
    try:
        df_processed_kpi = get_processed_table("alphavantage_processed_kpi")
        st.dataframe(df_processed_kpi, hide_index=True, width="stretch")
    except Exception as e:
        st.error(f"Could not load processed KPI data: {e}")

    st.subheader("Processed Pricing Data")
    try:
        df_processed_pricing = get_processed_table("alphavantage_pricing_processed")
        st.dataframe(df_processed_pricing, hide_index=True, width="stretch")
    except Exception as e:
        st.error(f"Could not load processed pricing data: {e}")

    st.divider()

    # ---------------------------------------------------------------
    # SECTION 3: User-created database tables
    # ---------------------------------------------------------------
    st.subheader("User-created Database Tables")
    st.markdown("These tables come from your uploaded CSV or Excel files.")

    try:
        user_tables = list_user_tables()
    except Exception as e:
        user_tables = []
        st.error(f"Could not list user tables: {e}")

    if not user_tables:
        st.info("No user tables found yet. Upload a CSV or Excel file to create one.")

    # Table selection
    chosen_table = st.selectbox("Select a table to view:", user_tables)

    if chosen_table:
        try:
            df_user_table = get_user_table(chosen_table)
            st.write(f"### Table: `{chosen_table}` — {len(df_user_table)} rows")
            st.dataframe(df_user_table, hide_index=True, width = "stretch")
        except Exception as e:
            st.error(f"Error loading table '{chosen_table}': {e}")
