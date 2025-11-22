import streamlit as st
from pathlib import Path
from datetime import datetime
from backend.data_model import TICKERS
from backend.scheduler import load_data, load_initial_data
from backend.database.db_functions import get_table, get_table_names, get_symbols_from_table
# Ordner der aktuellen Datei (z.B. app.py)
BASE_DIR = Path(__file__).resolve().parent

# Pfad zur PNG
img_path_fsbar = BASE_DIR.parent / "assets" / "finsightbar.png"
#__________________________Header____________________________

st.set_page_config(page_title="Data", page_icon="🔍")
#____________________________________________________________

#__________________________SIDEBAR___________________________
st.sidebar.subheader("Welcome to FinSight!")
st.sidebar.image(str(img_path_fsbar))
st.sidebar.divider()

if "load_data_time" in st.session_state:
    loaded_data_ts = st.session_state["load_data_time"]
else:
    st.session_state["load_data_time"] = "NOT NOW"
    loaded_data_ts = st.session_state["load_data_time"]

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


t_choice = st.sidebar.multiselect(
    "Choose Ticker",
    options=sorted(TICKERS))

st.session_state["chosen_tickers"] = t_choice

if st.sidebar.button("Download Ticker Data"):
    with st.spinner("Downloading data (this might take a while...)"):
        answer = load_data(t_choice)
        st.success(answer)



#____________________________________________________________

st.header("Alphavantage RAW-Data Table")
df = get_table("alphavantage_raw_kpi")
st.dataframe(df, hide_index=True)

st.header("Alphavantage PRICING Table")
df = get_table("alphavantage_daily_pricing")
st.dataframe(df, hide_index= True)
