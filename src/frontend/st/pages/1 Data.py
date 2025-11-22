import streamlit as st
import plotly.express as px
import pandas as pd
from pathlib import Path
from datetime import datetime
from backend.data_model import TICKERS
from backend.scheduler import load_data, load_initial_data
from backend.database.db_functions import get_table, get_table_names, get_symbols_from_table, get_unique_table
from backend.data_processing.alphavantage_processed import get_processed_table, process_alphavantage_raw_db
from backend.database.users_database import import_file_as_table, get_user_table, list_user_tables
import openpyxl
# Ordner der aktuellen Datei (z.B. app.py)
BASE_DIR = Path(__file__).resolve().parent

# Pfad zur PNG
img_path_fsbar = BASE_DIR.parent / "assets" / "finsightbar.png"
#__________________________Header____________________________

st.set_page_config(page_title="Data", page_icon="🔍")
#____________________________________________________________

tab1, tab2 = st.tabs(["Data Settings", "Analysis"])


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
        st.stop()

    # Table selection
    chosen_table = st.selectbox("Select a table to view:", user_tables)

    if chosen_table:
        try:
            df_user_table = get_user_table(chosen_table)
            st.write(f"### Table: `{chosen_table}` — {len(df_user_table)} rows")
            st.dataframe(df_user_table, hide_index=True, width = "stretch")
        except Exception as e:
            st.error(f"Error loading table '{chosen_table}': {e}")



with tab2:
    st.header("Market Analysis")

    # ---------------------------
    # 1. Pricing-Daten laden (mit Caching)
    # ---------------------------
    @st.cache_data(show_spinner=False)
    def load_pricing_data() -> pd.DataFrame:
        df = get_processed_table("alphavantage_pricing_processed")
        if isinstance(df, str):
            # get_processed_table gibt im Fehlerfall einen String zurück
            raise ValueError(df)
        if df.empty:
            raise ValueError("Die Tabelle 'alphavantage_pricing_processed' ist leer.")
        return df

    try:
        df_pricing = load_pricing_data()
    except Exception as e:
        st.error(f"❌ Konnte Pricing-Daten nicht laden: {e}")
        st.stop()

    # Datentyp & Sortierung
    if "date" not in df_pricing.columns or "symbol" not in df_pricing.columns:
        st.error("❌ Erwartete Spalten ('date', 'symbol') fehlen in den Pricing-Daten.")
        st.stop()

    df_pricing["date"] = pd.to_datetime(df_pricing["date"], errors="coerce")
    df_pricing = df_pricing.dropna(subset=["date"])
    df_pricing = df_pricing.sort_values(["symbol", "date"])

    symbols = sorted(df_pricing["symbol"].unique())
    if not symbols:
        st.info("Keine Symbole in den Pricing-Daten gefunden.")
        st.stop()

    # ---------------------------
    # 2. Symbol-Auswahl
    # ---------------------------
    st.subheader("🔎 Auswahl des Tickers")

    col_left, col_right = st.columns([2, 1])
    with col_left:
        chosen_symbol = st.selectbox(
            "Wähle ein Symbol für die Analyse:",
            symbols,
            index=0,
        )
    with col_right:
        st.write("")  # etwas Abstand
        st.metric("Anzahl verfügbarer Ticker", len(symbols))

    # ---------------------------
    # 3. Preis-Daten für Symbol
    # ---------------------------
    df_symbol = df_pricing[df_pricing["symbol"] == chosen_symbol].copy()

    if df_symbol.empty:
        st.warning(f"Keine Preisdaten für **{chosen_symbol}** gefunden.")
        st.stop()

    st.markdown(f"### 📈 Price Data for **{chosen_symbol}**")
    st.dataframe(
        df_symbol.sort_values("date", ascending=False),
        hide_index=True,
        width="stretch",
    )

    # ---------------------------
    # 4. Plotly Preis-Chart
    # ---------------------------
    import plotly.express as px

    st.markdown("#### Close Price Over Time")

    fig_price = px.line(
        df_symbol,
        x="date",
        y="close",
        title=f"{chosen_symbol} – Close Price over Time",
        markers=True,
        labels={"date": "Date", "close": "Close Price"},
        template="plotly_white",
    )
    fig_price.update_layout(margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_price, width="stretch")

    with st.expander("Weitere Preis-Ansichten (Open / High / Low / Close)"):
        fig_multi = px.line(
            df_symbol,
            x="date",
            y=["open", "high", "low", "close"],
            title=f"{chosen_symbol} – OHLC Price Overview",
            labels={"value": "Price", "date": "Date", "variable": "Type"},
            template="plotly_white",
        )
        fig_multi.update_layout(margin=dict(l=10, r=10, t=40, b=10))
        st.plotly_chart(fig_multi, width="stretch")

    st.divider()

    # ---------------------------
    # 5. Korrelationsanalyse
    # ---------------------------
    st.header("📈 Correlation Analysis")

    st.markdown(
        "Analysiere die Korrelation täglicher Renditen zwischen mehreren Symbolen."
    )

    selected_corr_symbols = st.multiselect(
        "Wähle Symbole für die Korrelationsanalyse:",
        symbols,
        default=symbols[: min(5, len(symbols))],
    )

    if len(selected_corr_symbols) < 2:
        st.info("Bitte mindestens zwei Symbole auswählen, um eine Korrelation zu berechnen.")
        st.stop()

    df_corr = df_pricing[df_pricing["symbol"].isin(selected_corr_symbols)].copy()

    # Pivot: Zeilen = Date, Spalten = Symbol, Werte = Close
    df_pivot = (
        df_corr.pivot(index="date", columns="symbol", values="close")
        .sort_index()
        .dropna(how="any")
    )

    if df_pivot.empty or df_pivot.shape[0] < 2:
        st.warning("Zu wenige gemeinsame Datenpunkte für die gewählten Symbole.")
        st.stop()

    # Daily returns
    df_returns = df_pivot.pct_change().dropna(how="any")

    if df_returns.empty:
        st.warning("Zu wenige Renditedaten zur Korrelationsberechnung.")
        st.stop()

    corr_matrix = df_returns.corr()

    st.markdown("### Korrelationsmatrix (Daily Returns)")
    st.dataframe(corr_matrix.round(3), width="stretch")

    # Plotly Heatmap
    import plotly.figure_factory as ff

    fig_corr = ff.create_annotated_heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns.tolist(),
        y=corr_matrix.index.tolist(),
        colorscale="Blues",
        showscale=True,
        zmin=-1,
        zmax=1,
    )
    fig_corr.update_layout(
        title="Correlation Heatmap",
        margin=dict(l=10, r=10, t=40, b=10),
    )
    st.plotly_chart(fig_corr, width="stretch")