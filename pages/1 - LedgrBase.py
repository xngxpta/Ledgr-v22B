# __author__ = 'R. Sengupta | r_xn'
# __copyright__ = 'Copyright 2023, Ledgr | www.alphaLedgr.com'
# __credits__ = ['r_xn, s.sengupta, prithvirajsengupta033@gmail.com]
# __license__ = 'Ledgr | alphaledgr.com'
# __version__ = '01.02.04'
# __maintainer__ = 'r_xn@alphaledgr.com'
# __emails__ = 'r_xn@alphaledgr.com / response@alphaledgr.com'
# __status__ = 'In active development'
import numpy as np
import pandas as pd
import datetime as dt
import plotly.express as px
import yfinance as yf

from mftool import Mftool
import plotly.graph_objs as go
import os
import requests
import io
import matplotlib as plt
from plotly.subplots import make_subplots
from selectolax.parser import HTMLParser
import requests
import streamlit as st
import streamlit.components.v1 as components

from datetime import date, timedelta



st.set_page_config(
    page_title="LedgrBase | Your Asset Dossier",
    layout="wide",
    initial_sidebar_state="expanded",
)
# ##################################################################

direc = os.getcwd()

logofile = f"{direc}/pages/appdata/imgs/Ledgr_Logo_F2.png"
st.logo(logofile, size="medium", link='https://alphaledgr.com/',
        icon_image=logofile)
url_stripe = "https://buy.stripe.com/6oU28t21Y2NmbfjdkK0480h"
url_stripe_2 = "https://buy.stripe.com/dR64iacsh6bx9zi5kk"
st.sidebar.image(logofile)
st.sidebar.caption("View Markets, get info on funds & monitor your Holdings!")
st.sidebar.link_button("Join Us!", url_stripe_2, type="primary",
                       disabled=False, use_container_width=True)
start_date = dt.datetime(2021, 1, 1)
end_date = dt.datetime.today()
altstart = dt.datetime(2023, 1, 1)
indlist = pd.read_csv(f"{direc}/pages/appdata/Index_L.csv")["Symbol"]
indlist = pd.Series(indlist)
etflist = pd.read_csv(f"{direc}/pages/appdata/ETF_L.csv")["Symbol"]
tickerl = pd.read_csv(f"{direc}/pages/appdata/tickerlist_y.csv")["SYMBOL"]
curr_list = pd.read_csv(f"{direc}/pages/appdata/currency_list.csv")["Symbol"]
mfptions = ['Get Quote for a Fund', 'Get NAV History for a Fund', 'Get Fund Details']
# ####################################################
# Icons and Links ###########################
ytube = f"{direc}/pages/appdata/imgs/ytube.svg"
fbook = f"{direc}/pages/appdata/imgs/fbook.svg"
insta = f"{direc}/pages/appdata/imgs/insta.svg"
linkedin = f"{direc}/pages/appdata/imgs/linkedin.svg"
ledgrblog = f"{direc}/pages/appdata/imgs/Ledgr_Logo_F1.png"
icon_size = 100  

# ####################################
nx1, nx2, nx3 = st.columns([2, 4, 2])
with nx1:
    st.write(' ')
with nx2:
    st.title(":MarketBoard:")
    st.markdown("""**Your Wealth Dashboard and Global Finances**""")
with nx3:
    st.write(' ')


# ###################################
@st.cache_resource
def data_BSE():
    BSE = yf.Ticker("^BSESN")
    df_BSE = BSE.history(period="5y")
    figOHLC_BSE = go.Figure()
    figOHLC_BSE.add_trace(
        go.Ohlc(
            x=df_BSE.index,
            open=df_BSE["Open"],
            high=df_BSE["High"],
            low=df_BSE["Low"],
            close=df_BSE["Close"],
            name="SENSEX",
        )
    )
    figOHLC_BSE.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_BSE, figOHLC_BSE


df_BSE, figOHLC_BSE = data_BSE()


@st.cache_resource
def data_NSEI():
    nse = yf.Ticker("^NSEI")
    df_NSEI = nse.history(period="5y")
    figOHLC_NSEI = go.Figure()
    figOHLC_NSEI.add_trace(
        go.Ohlc(
            x=df_NSEI.index,
            open=df_NSEI["Open"],
            high=df_NSEI["High"],
            low=df_NSEI["Low"],
            close=df_NSEI["Close"],
            name="NIFTY50",
        )
    )
    figOHLC_NSEI.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_NSEI, figOHLC_NSEI


df_NSEI, figOHLC_NSEI = data_NSEI()


@st.cache_resource
def data_SPX():
    spx = yf.Ticker("^GSPC")
    df_SPX = spx.history(period="5y")
    figOHLC_SPX = go.Figure()
    figOHLC_SPX.add_trace(
        go.Ohlc(
            x=df_SPX.index,
            open=df_SPX["Open"],
            high=df_SPX["High"],
            low=df_SPX["Low"],
            close=df_SPX["Close"],
            name="SPX",
        )
    )
    figOHLC_SPX.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_SPX, figOHLC_SPX


df_SPX, figOHLC_SPX = data_SPX()


@st.cache_resource
def data_DAX():
    dax = yf.Ticker("^GDAXI")
    df_DAX = dax.history(period="5y")
    figOHLC_DAX = go.Figure()
    figOHLC_DAX.add_trace(
        go.Ohlc(
            x=df_DAX.index,
            open=df_DAX["Open"],
            high=df_DAX["High"],
            low=df_DAX["Low"],
            close=df_DAX["Close"],
            name="DAX",
        )
    )
    figOHLC_DAX.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_DAX, figOHLC_DAX


df_DAX, figOHLC_DAX = data_DAX()


@st.cache_resource
def data_CAC():
    cac = yf.Ticker("^FCHI")
    df_CAC = cac.history(period="5y")
    figOHLC_CAC = go.Figure()
    figOHLC_CAC.add_trace(
        go.Ohlc(
            x=df_CAC.index,
            open=df_CAC["Open"],
            high=df_CAC["High"],
            low=df_CAC["Low"],
            close=df_CAC["Close"],
            name="CAC40",
        )
    )
    figOHLC_CAC.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_CAC, figOHLC_CAC


df_CAC, figOHLC_CAC = data_CAC()


@st.cache_resource
def data_DJIA():
    dji = yf.Ticker("^DJI")
    df_DJIA = dji.history(period="5y")
    figOHLC_DJIA = go.Figure()
    figOHLC_DJIA.add_trace(
        go.Ohlc(
            x=df_DJIA.index,
            open=df_DJIA["Open"],
            high=df_DJIA["High"],
            low=df_DJIA["Low"],
            close=df_DJIA["Close"],
            name="DJIA",
        )
    )
    figOHLC_DJIA.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_DJIA, figOHLC_DJIA


df_DJIA, figOHLC_DJIA = data_DJIA()


@st.cache_resource
def data_TYO():
    tyo = yf.Ticker("^N225")
    df_tyo = tyo.history(period="5y")
    figOHLC_tyo = go.Figure()
    figOHLC_tyo.add_trace(
        go.Ohlc(
            x=df_tyo.index,
            open=df_tyo["Open"],
            high=df_tyo["High"],
            low=df_tyo["Low"],
            close=df_tyo["Close"],
            name="TYO",
        )
    )
    figOHLC_tyo.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_tyo, figOHLC_tyo


df_tyo, figOHLC_tyo = data_TYO()


@st.cache_resource
def data_FTSE():
    FTSE = yf.Ticker("^FTSE")
    df_FTSE = FTSE.history(period="5y")
    figOHLC_FTSE = go.Figure()
    figOHLC_FTSE.add_trace(
        go.Ohlc(
            x=df_FTSE.index,
            open=df_FTSE["Open"],
            high=df_FTSE["High"],
            low=df_FTSE["Low"],
            close=df_FTSE["Close"],
            name="FTSE",
        )
    )
    figOHLC_FTSE.update_layout(xaxis_rangeslider_visible=False, showlegend=True)
    return df_FTSE, figOHLC_FTSE


df_FTSE, figOHLC_FTSE = data_FTSE()


@st.cache_resource
def data_mkt():
    df_mk = pd.DataFrame()
    df_mk["SENSEX"] = df_BSE["Close"]
    df_mk["NSEI"] = df_NSEI["Close"]
    df_mk["DAX"] = df_DAX["Close"]
    df_mk["CAC"] = df_CAC["Close"]
    df_mk["SPX"] = df_SPX["Close"]
    df_mk["FTSE"] = df_FTSE["Close"]
    df_mk["N225"] = df_tyo["Close"]
    fig_mkt = go.Figure()
    fig_mkt.add_trace(
        go.Scatter(x=df_NSEI.index, y=df_NSEI["Close"], mode="lines", name="NSEI")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_BSE.index, y=df_BSE["Close"], mode="lines", name="SENSEX")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_DAX.index, y=df_DAX["Close"], mode="lines", name="DAX")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_CAC.index, y=df_CAC["Close"], mode="lines", name="CAC")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_SPX.index, y=df_SPX["Close"], mode="lines", name="SPX")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_DJIA.index, y=df_DJIA["Close"], mode="lines", name="DJIA")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_FTSE.index, y=df_FTSE["Close"], mode="lines", name="FTSE")
    )
    fig_mkt.add_trace(
        go.Scatter(x=df_tyo.index, y=df_tyo["Close"], mode="lines", name="N225")
    )
    fig_mkt.update_xaxes(visible=True, showticklabels=True)
    fig_mkt.update_yaxes(visible=True, showticklabels=True)

    return df_mk, fig_mkt


df_mk, fig_mkt = data_mkt()
multi_symbols = ["^IXIC", "^GSPC", "^NYA", "^BSESN", "^NSEI", "^NSEBANK"]
multi_details = [
    "NASDAQ Composite",
    "S&P500",
    "NYSE Composite (DJ)",
    "BSE SENSEX",
    "NIFTY50",
    "NIFTYBANK",
]

multi_index_list = pd.DataFrame(
    {"Symbol": multi_symbols, "Exchange Index": multi_details}
)


@st.cache_resource
def treasury():
    trs = yf.Ticker("^TYX")
    df_treasury = trs.history(period="5y")
    fig_treasury = go.Figure()
    fig_treasury.add_trace(
        go.Ohlc(
            x=df_treasury.index,
            open=df_treasury["Open"],
            high=df_treasury["High"],
            low=df_treasury["Low"],
            close=df_treasury["Close"],
        )
    )
    fig_treasury.update_xaxes(visible=True, showticklabels=True)
    fig_treasury.update_yaxes(
        title="US Treasury Yield", visible=True, showticklabels=True
    )
    fig_treasury.update_layout(xaxis_rangeslider_visible=False, showlegend=False)
    return df_treasury, fig_treasury


df_treasury, fig_treasury = treasury()


@st.cache_resource
def vix():
    vix = yf.Ticker("^VIX")
    df_vix = vix.history(period="5y")
    # df_vix = df_vix.drop(['Volume'], axis=1)
    fig_vix = go.Figure()
    fig_vix.add_trace(
        go.Candlestick(
            x=df_vix.index,
            open=df_vix["Open"],
            high=df_vix["High"],
            low=df_vix["Low"],
            close=df_vix["Close"],
            name="VIX",
        )
    )
    fig_vix.update_traces(increasing_line_color="cyan", decreasing_line_color="red")
    fig_vix.update_layout(xaxis_rangeslider_visible=False)
    fig_vix.update_xaxes(visible=True, showticklabels=True)
    fig_vix.update_yaxes(title="VIX", visible=True, showticklabels=True)
    # fig_vix.update_layout(height=360, showlegend=False)
    return df_vix, fig_vix


df_vix, fig_vix = vix()


@st.cache_resource
def ivix():
    ivix = yf.Ticker("^INDIAVIX")
    df_ivix = ivix.history(period="5y")
    # df_vix = df_vix.drop(['Volume'], axis=1)
    fig_ivix = go.Figure()
    fig_ivix.add_trace(
        go.Candlestick(
            x=df_ivix.index,
            open=df_ivix["Open"],
            high=df_ivix["High"],
            low=df_ivix["Low"],
            close=df_ivix["Close"],
            name="INDIAVIX",
        )
    )
    fig_ivix.update_traces(increasing_line_color="blue", decreasing_line_color="gray")
    fig_ivix.update_layout(xaxis_rangeslider_visible=False)
    fig_ivix.update_xaxes(visible=True, showticklabels=True)
    fig_ivix.update_yaxes(title="INDIAVIX", visible=True, showticklabels=True)

    return df_ivix, fig_ivix


df_ivix, fig_ivix = ivix()



@st.cache_resource

def get_historical_price(ticker, target_date):
    """
    Get the closing price for a ticker on target_date.

    If target_date is a weekend/market holiday, the function
    looks backwards for the most recent available trading day.
    """

    try:
        stock = yf.Ticker(ticker)

        start_date = target_date - timedelta(days=7)
        end_date = target_date + timedelta(days=1)

        history = stock.history(
            start=start_date,
            end=end_date,
            auto_adjust=False
        )

        if history.empty:
            return None

        # Remove timezone information if present
        history.index = history.index.tz_localize(None)

        # Keep dates on or before the requested date
        history = history[
            history.index.date <= target_date
        ]

        if history.empty:
            return None

        # Most recent available trading day
        latest_row = history.iloc[-1]

        return float(latest_row["Close"])

    except Exception as e:
        st.error(f"Could not retrieve historical price for {ticker}: {e}")
        return None


def get_current_price(ticker):
    """
    Get the latest available market price.
    """
    def get_price_history(ticker, start_date, end_date):
    """
    Retrieve daily closing prices for a security.
    """

    try:
        stock = yf.Ticker(ticker)

        # Add one day because yfinance's end date is exclusive
        history = stock.history(
            start=start_date,
            end=end_date + timedelta(days=1),
            auto_adjust=False
        )

        if history.empty:
            return pd.Series(dtype=float)

        prices = history["Close"].copy()

        # Remove timezone information
        if prices.index.tz is not None:
            prices.index = prices.index.tz_localize(None)

        prices.index = prices.index.date

        return prices

    except Exception as e:
        st.error(
            f"Could not retrieve performance data "
            f"for {ticker}: {e}"
        )

        return pd.Series(dtype=float)

    def calculate_cumulative_performance(portfolio_df):
    """
    Calculate daily cumulative portfolio performance.
    """

    performance_data = []

    today = date.today()

    for _, security in portfolio_df.iterrows():

        ticker = security["Purchased Security"]
        units = security["Units Held"]
        start_date = security["Portfolio Start Date"]
        release_date = security["Release Date"]

        # ----------------------------------------------------
        # Determine the final date to use
        # ----------------------------------------------------

        if security["Status"] == "open":
            end_date = today
        else:
            end_date = min(release_date, today)

        # ----------------------------------------------------
        # Get historical prices
        # ----------------------------------------------------

        prices = get_price_history(
            ticker,
            start_date,
            end_date
        )

        if prices.empty:
            continue

        # ----------------------------------------------------
        # Calculate position value
        # ----------------------------------------------------

        position_data = pd.DataFrame({
            "Date": prices.index,
            "Ticker": ticker,
            "Position Value": prices.values * units,
            "Units": units
        })

        performance_data.append(position_data)

    if not performance_data:
        return pd.DataFrame()

    # --------------------------------------------------------
    # Combine all securities
    # --------------------------------------------------------

    all_positions = pd.concat(
        performance_data,
        ignore_index=True
    )

    # --------------------------------------------------------
    # Aggregate portfolio value by date
    # --------------------------------------------------------

    portfolio_value = (
        all_positions
        .groupby("Date")["Position Value"]
        .sum()
        .reset_index()
    )

    portfolio_value.rename(
        columns={
            "Position Value": "Portfolio Value"
        },
        inplace=True
    )

    # --------------------------------------------------------
    # Calculate cumulative P&L
    # --------------------------------------------------------

    initial_value = portfolio_value[
        "Portfolio Value"
    ].iloc[0]

    portfolio_value["Cumulative P&L"] = (
        portfolio_value["Portfolio Value"]
        - initial_value
    )

    portfolio_value["Cumulative Return %"] = (
        portfolio_value["Cumulative P&L"]
        / initial_value
    ) * 100

    return portfolio_value

    try:
        stock = yf.Ticker(ticker)

        history = stock.history(
            period="5d",
            auto_adjust=False
        )

        if history.empty:
            return None

        return float(history["Close"].dropna().iloc[-1])

    except Exception as e:
        st.error(f"Could not retrieve current price for {ticker}: {e}")
        return None


def calculate_security_data(
    portfolio_name,
    portfolio_start_date,
    ticker,
    units_held,
    release_date
):
    """
    Calculate all portfolio information for one security.
    """

    ticker = ticker.upper().strip()

    # --------------------------------------------------------
    # STATUS
    # --------------------------------------------------------

    if release_date == date.today():
        status = "open"
    else:
        status = "closed"

    # --------------------------------------------------------
    # PURCHASE PRICE
    # --------------------------------------------------------

    purchase_price = get_historical_price(
        ticker,
        portfolio_start_date
    )

    # --------------------------------------------------------
    # SELLING PRICE
    # --------------------------------------------------------

    if status == "open":
        # Position is open, so use current market price
        selling_price = get_current_price(ticker)

    else:
        # Position is closed, so use release-date price
        selling_price = get_historical_price(
            ticker,
            release_date
        )

    # --------------------------------------------------------
    # PROFIT / LOSS
    # --------------------------------------------------------

    if purchase_price is not None and selling_price is not None:

        investment_value = purchase_price * units_held
        current_or_sale_value = selling_price * units_held

        profit_loss = (
            selling_price - purchase_price
        ) * units_held

        profit_loss_percent = (
            (selling_price - purchase_price)
            / purchase_price
        ) * 100

    else:
        investment_value = None
        current_or_sale_value = None
        profit_loss = None
        profit_loss_percent = None

    # --------------------------------------------------------
    # RETURN DATA
    # --------------------------------------------------------

    return {
        "Portfolio Name": portfolio_name,
        "Portfolio Start Date": portfolio_start_date,
        "Purchased Security": ticker,
        "Units Held": units_held,
        "Release Date": release_date,
        "Status": status,
        "Purchase Price": purchase_price,
        "Selling Price": selling_price,
        "Investment Value": investment_value,
        "Current / Sale Value": current_or_sale_value,
        "Profit / Loss": profit_loss,
        "Profit / Loss %": profit_loss_percent
    }


# ============================================================
# APPLICATION TITLE
# ============================================================
with st.container(border=True):
    hh1, hh2 = st.columns([2, 3])
    with hh1:
        st.title(": LedgrBase :")
        st.subheader("Hi User!")
        st.subheader("Welcome to Ledgr!")
        st.write("Organize your asset-holdings here, track their performance!")
    with hh2:
        st.video("https://youtu.be/m8C4C-LW3YY?si=wOMwU7yKp-UMYuQO")


st.header("📈 Security Portfolio Manager")

st.write(
    "Track your investment portfolio and monitor the "
    "profit or loss of individual securities."
)


# ============================================================
# MAIN USER CHOICE
# ============================================================

user_choice = st.selectbox(
    "What would you like to do?",
    [
        "Select an option",
        "Track the Performance of my Portfolio",
        "Continue observing the markets"
    ]
)


# ============================================================
# OPTION 2 — MARKET OBSERVATION
# ============================================================

if user_choice == "Continue observing the markets":

    st.info(
        "Market observation mode selected. "
        "No portfolio tracking action is required."
    )


# ============================================================
# OPTION 1 — PORTFOLIO TRACKING
# ============================================================

elif user_choice == "Track the Performance of my Portfolio":

    st.subheader("Portfolio Details")

    # --------------------------------------------------------
    # BASIC PORTFOLIO INFORMATION
    # --------------------------------------------------------

    portfolio_name = st.text_input(
        "A. Portfolio Name",
        placeholder="e.g. Long Term Growth Portfolio"
    )

    portfolio_start_date = st.date_input(
        "B. Portfolio Start Date",
        value=date.today()
    )

    # --------------------------------------------------------
    # NUMBER OF SECURITIES
    # --------------------------------------------------------

    number_of_securities = st.number_input(
        "Number of securities in the portfolio",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

    st.subheader("Security Details")

    # --------------------------------------------------------
    # MULTIPLE SECURITY FORM
    # --------------------------------------------------------

    with st.form("portfolio_form"):

        security_inputs = []

        for i in range(number_of_securities):

            st.markdown(f"### Security {i + 1}")

            col1, col2, col3 = st.columns(3)

            with col1:
                ticker = st.text_input(
                    "C. Stock Ticker",
                    placeholder="e.g. AAPL",
                    key=f"ticker_{i}"
                )

            with col2:
                units = st.number_input(
                    "D. Units Held",
                    min_value=0.0,
                    value=1.0,
                    step=1.0,
                    key=f"units_{i}"
                )

            with col3:
                release_date = st.date_input(
                    "E. Release Date",
                    value=date.today(),
                    key=f"release_date_{i}"
                )

            security_inputs.append({
                "ticker": ticker,
                "units": units,
                "release_date": release_date
            })

        submit_button = st.form_submit_button(
            "Create / Update Portfolio",
            type="primary"
        )

    # ========================================================
    # PROCESS FORM
    # ========================================================

    if submit_button:

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not portfolio_name.strip():

            st.error("Please enter a Portfolio Name.")
            st.stop()

        valid_securities = []

        for security in security_inputs:

            if not security["ticker"].strip():

                st.error(
                    "Please enter a ticker for every security."
                )
                st.stop()

            if security["units"] <= 0:

                st.error(
                    "Units Held must be greater than zero."
                )
                st.stop()

            valid_securities.append(security)

        # ----------------------------------------------------
        # CREATE PORTFOLIO DATA
        # ----------------------------------------------------

        portfolio_data = []

        progress_bar = st.progress(0)

        for index, security in enumerate(valid_securities):

            with st.spinner(
                f"Retrieving data for "
                f"{security['ticker'].upper()}..."
            ):

                row = calculate_security_data(
                    portfolio_name=portfolio_name,
                    portfolio_start_date=portfolio_start_date,
                    ticker=security["ticker"],
                    units_held=security["units"],
                    release_date=security["release_date"]
                )

                portfolio_data.append(row)

            progress_bar.progress(
                (index + 1) / len(valid_securities)
            )

        progress_bar.empty()

        # ----------------------------------------------------
        # CREATE DATAFRAME
        # ----------------------------------------------------

        portfolio_df = pd.DataFrame(
            portfolio_data
        )

        # ----------------------------------------------------
        # STORE DATAFRAME IN SESSION STATE
        # ----------------------------------------------------

        st.session_state["portfolio_df"] = portfolio_df


# ============================================================
# DISPLAY PORTFOLIO
# ============================================================

if "portfolio_df" in st.session_state:
    # ============================================================
# CUMULATIVE PERFORMANCE
# ============================================================

st.divider()

st.header("📊 Cumulative Portfolio Performance")

with st.spinner("Calculating historical portfolio performance..."):

    performance_df = calculate_cumulative_performance(
        portfolio_df
    )


if not performance_df.empty:

    # --------------------------------------------------------
    # Portfolio Value Chart
    # --------------------------------------------------------

    st.subheader("Portfolio Value Over Time")

    value_chart_df = performance_df.copy()

    value_chart_df["Date"] = pd.to_datetime(
        value_chart_df["Date"]
    )

    value_chart_df = value_chart_df.set_index(
        "Date"
    )

    st.line_chart(
        value_chart_df["Portfolio Value"],
        use_container_width=True
    )


    # --------------------------------------------------------
    # Cumulative P&L Chart
    # --------------------------------------------------------

    st.subheader("Cumulative Profit / Loss")

    pnl_chart_df = performance_df.copy()

    pnl_chart_df["Date"] = pd.to_datetime(
        pnl_chart_df["Date"]
    )

    pnl_chart_df = pnl_chart_df.set_index(
        "Date"
    )

    st.line_chart(
        pnl_chart_df["Cumulative P&L"],
        use_container_width=True
    )


    # --------------------------------------------------------
    # Cumulative Return %
    # --------------------------------------------------------

    st.subheader("Cumulative Return (%)")

    return_chart_df = performance_df.copy()

    return_chart_df["Date"] = pd.to_datetime(
        return_chart_df["Date"]
    )

    return_chart_df = return_chart_df.set_index(
        "Date"
    )

    st.line_chart(
        return_chart_df["Cumulative Return %"],
        use_container_width=True
    )


    # --------------------------------------------------------
    # Performance Data
    # --------------------------------------------------------

    with st.expander("View Performance Data"):

        st.dataframe(
            performance_df,
            use_container_width=True,
            hide_index=True
        )

else:

    st.warning(
        "Historical performance data could not be calculated."
    )

    portfolio_df = st.session_state["portfolio_df"]

    st.divider()

    st.header("Portfolio Performance")


    # ========================================================
    # PORTFOLIO DATAFRAME
    # ========================================================

    st.subheader("Portfolio Holdings")

    display_df = portfolio_df.copy()

    # Format prices
    for column in [
        "Purchase Price",
        "Selling Price",
        "Investment Value",
        "Current / Sale Value",
        "Profit / Loss"
    ]:

        display_df[column] = display_df[column].apply(
            lambda x: f"₹{x:,.2f}"
            if pd.notna(x)
            else "N/A"
        )

    # Format P&L %
    display_df["Profit / Loss %"] = display_df[
        "Profit / Loss %"
    ].apply(
        lambda x: f"{x:.2f}%"
        if pd.notna(x)
        else "N/A"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # PORTFOLIO METRICS
    # ========================================================

    valid_pnl = portfolio_df[
        portfolio_df["Profit / Loss"].notna()
    ]

    total_investment = portfolio_df[
        "Investment Value"
    ].sum()

    total_current_or_sale_value = portfolio_df[
        "Current / Sale Value"
    ].sum()

    total_profit_loss = portfolio_df[
        "Profit / Loss"
    ].sum()


    if total_investment != 0:

        total_profit_loss_percent = (
            total_profit_loss
            / total_investment
        ) * 100

    else:

        total_profit_loss_percent = 0


    open_positions = portfolio_df[
        portfolio_df["Status"] == "open"
    ]

    closed_positions = portfolio_df[
        portfolio_df["Status"] == "closed"
    ]


    # ========================================================
    # METRIC CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Total Invested",
            f"₹{total_investment:,.2f}"
        )

    with col2:

        st.metric(
            "Current / Sale Value",
            f"₹{total_current_or_sale_value:,.2f}"
        )

    with col3:

        st.metric(
            "Total P&L",
            f"₹{total_profit_loss:,.2f}",
            delta=f"{total_profit_loss_percent:.2f}%"
        )

    with col4:

        st.metric(
            "Securities",
            len(portfolio_df)
        )


    # ========================================================
    # OPEN / CLOSED POSITIONS
    # ========================================================

    st.subheader("Position Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Open Positions",
            len(open_positions)
        )

    with col2:

        st.metric(
            "Closed Positions",
            len(closed_positions)
        )


    # ========================================================
    # PROFITABLE / LOSS-MAKING SECURITIES
    # ========================================================

    st.subheader("Security-Level Performance")

    profitable = valid_pnl[
        valid_pnl["Profit / Loss"] > 0
    ]

    loss_making = valid_pnl[
        valid_pnl["Profit / Loss"] < 0
    ]

    unchanged = valid_pnl[
        valid_pnl["Profit / Loss"] == 0
    ]


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Profitable Securities",
            len(profitable)
        )

    with col2:

        st.metric(
            "Loss-Making Securities",
            len(loss_making)
        )

    with col3:

        st.metric(
            "Unchanged Securities",
            len(unchanged)
        )


    # ========================================================
    # DOWNLOAD DATA
    # ========================================================

    st.subheader("Export Portfolio")

    csv = portfolio_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Portfolio as CSV",
        data=csv,
        file_name=f"{portfolio_df['Portfolio Name'].iloc[0]}.csv",
        mime="text/csv"
    )


# Mutual Funds ##
@st.cache_data(ttl=3600)  # Caches the data for 1 hour to prevent redundant heavy network calls
def fetch_amfi_master_data():
  url = "https://amfiindia.com"
  try:
    response = requests.get(url, timeout=10)
    raw_text = response.text

    # Parse semicolon-separated values while filtering out empty rows/headers
    lines = []
    for line in raw_text.splitlines():
      if ";" in line and "Scheme Code" not in line:
        lines.append(line)

    csv_data = "\n".join(lines)
    columns = [
        "Scheme Code",
        "ISIN Growth",
        "ISIN Reinvestment",
        "Scheme Name",
        "Net Asset Value",
        "Date",
    ]
    df = pd.read_csv(io.StringIO(csv_data), sep=";", names=columns)

    # Clean data types
    df["Net Asset Value"] = pd.to_numeric(
        df["Net Asset Value"], errors="coerce"
    )
    df["Scheme Code"] = df["Scheme Code"].astype(str).str.strip()
    df["Scheme Name"] = df["Scheme Name"].astype(str).str.strip()
    df = df.dropna(subset=["Net Asset Value"])
    return df
  except Exception as e:
    st.error(f"Error connecting to AMFI servers: {e}")
    return pd.DataFrame()


@st.cache_data(ttl=1800)
def fetch_historical_nav_data(mfselected):
  # Pull historical entries from the free MFapi endpoint using the clean AMFI ID
  url = f"https://mfapi.in{mfselected}"
  try:
    response = requests.get(url, timeout=10)
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
      df_hist = pd.DataFrame(data["data"])
      df_hist["date"] = pd.to_datetime(df_hist["date"], format="%d-%m-%Y")
      df_hist["nav"] = df_hist["nav"].astype(float)
      return df_hist.sort_values(by="date")
  except Exception:
    pass
  return pd.DataFrame()



# ####################### ##############################


st.write("    ----    ")



st.write("    ----    ")

with st.container(border=True):
    st.title(":MarketBoard:")
    hg1, hg2 = st.columns([2, 3])
    with hg1:
        st.subheader("Follow, Track and Global Markets")
        st.caption("Explore Indices, Exchange Traded & Mutual Funds and more!")
    with hg2:
        st.video("https://youtu.be/E9xCapIwd7o?si=RtB3c3ptgVTZ05-C")

with st.container(border=True):
    st.header("A. Markets & Exchanges", divider='rainbow')
    st.info(
        """ Compare Global Markets. Investigate each Markets performance
    in the tabs which follow"""
    )
    tabs = [
        "Global Markets",
        "NSE - IN",
        "BSE - SENSEX",
        "SPX - USA",
        "DAX - GDR",
        "CAC40 - FR",
        "Dow Jones - US",
        "Nikkei225 - JPN",
        "FTSE - UK",
    ]
    tub0, tub1, tub1A, tub2, tub3, tub4, tub5, tub6, tub7 = st.tabs(tabs)
    with tub0:
        st.plotly_chart(fig_mkt, use_container_width=True)
    with tub1:
        st.plotly_chart(figOHLC_NSEI, use_container_width=True)
    with tub1A:
        st.plotly_chart(figOHLC_BSE, use_container_width=True)
    with tub2:
        df_SPX, figOHLC_SPX = data_SPX()
        st.plotly_chart(figOHLC_SPX, use_container_width=True)
    with tub3:
        st.plotly_chart(figOHLC_DAX, use_container_width=True)
    with tub4:
        st.plotly_chart(figOHLC_CAC, use_container_width=True)
    with tub5:
        st.plotly_chart(figOHLC_DJIA, use_container_width=True)
    with tub6:
        st.plotly_chart(figOHLC_tyo, use_container_width=True)
    with tub7:
        st.plotly_chart(figOHLC_FTSE, use_container_width=True)



with st.container(border=True):
    st.subheader("B. SIP Calculator", divider='rainbow')
    st.caption(
        "Find out your Returns from any SIP scheme against a one-time investment"
    )
    with st.form("sipcalc"):
        A = st.slider(
            "Enter the monthly SIP amount: ",
            min_value=500,
            max_value=9900,
            value=1050,
            step=100,
            help="Input your monthly payments installments here!",
        )
        YR = st.slider(
            "Enter the yearly Rate of Return in pct: ",
            min_value=5,
            max_value=20,
            value=10,
            step=1,
            help="Indicate your scheme's Return Rate[ref:IRR/XIRR]",
        )
        Y = st.slider(
            "Enter the number of years: ",
            min_value=2,
            max_value=15,
            value=5,
            step=1,
            help="Indicate the number of years of investing",
        )
        submitted = st.form_submit_button("Calculate Returns >> ")
        if submitted:
            MR = YR / 12 / 100
            M = Y * 12
            FV = A * ((((1 + MR) ** (M)) - 1) * (1 + MR)) / MR
            FV = round(FV)
            gh2, gh3 = st.columns(2)
            with gh2:
                st.subheader("Your Expected Returns are: - ")
            with gh3:
                st.metric("Returns [INR]", FV)
        else:
            st.warning("Select values and click Calculate Returns")
st.write("    ------    ")



@st.cache_resource
def etf(etfselect):
    etfselect1 = etfselect + ".NS"
    etf = yf.Ticker(etfselect1)
    df_etf = etf.history(period="5y")
    figOHLC_etf = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.2,
        subplot_titles=("NAV Price Movement", "Traded Volume"),
        row_width=[0.2, 0.7],
    )
    figOHLC_etf.add_trace(
        go.Ohlc(
            x=df_etf.index,
            open=df_etf["Open"],
            high=df_etf["High"],
            low=df_etf["Low"],
            close=df_etf["Close"],
            name=f"OHLC for {etfselect}",
        ),
        row=1,
        col=1,
    )
    figOHLC_etf.add_trace(
        go.Bar(
            x=df_etf.index, y=df_etf["Volume"], name="Volume Traded", showlegend=False
        ),
        row=2,
        col=1,
    )
    figOHLC_etf.update_layout(xaxis_rangeslider_visible=False)
    figOHLC_etf.update_layout(showlegend=False)
    return figOHLC_etf, df_etf


@st.cache_resource
def currency(currency_selected):
    curr = yf.Ticker(currency_selected)
    currency_df = curr.history(period="3y")
    currency_df1 = currency_df.filter(["Open", "High", "Low", "Close"], axis=1)
    fig_currency1 = go.Figure()
    fig_currency1.add_trace(
        go.Ohlc(
            x=currency_df1.index,
            open=currency_df1["Open"],
            high=currency_df1["High"],
            low=currency_df1["Low"],
            close=currency_df1["Close"],
        )
    )
    fig_currency1.update_xaxes(visible=True, showticklabels=True)
    fig_currency1.update_yaxes(
        title="Exchange Ratio", visible=True, showticklabels=True
    )
    fig_currency1.update_layout(xaxis_rangeslider_visible=False, height=360)
    return currency_df1, fig_currency1


url_ytube = "https://www.youtube.com/@LedgrBase"
url_fb = "https://www.facebook.com/share/1BnXaYvRzV/"
url_insta = "https://www.instagram.com/alphaledgr/"
url_blog = "https://www.alphaledgr.com/Blog"
url_linkedin = "https://www.linkedin.com/company/ledgrapp/"

with st.container(border=True):
    st.header("C. Exchange Traded Funds", divider='rainbow')
    etfselect = st.selectbox("Please select ETF here!", etflist)
    figOHLC_etf, df_etf = etf(etfselect)
    st.plotly_chart(figOHLC_etf, use_container_width=True)
st.write("   ----   ")

with st.container(border=True):
    st.header("D. Currencies", divider='rainbow')
    currency_selected = st.selectbox("Select Currency Pair", curr_list)
    currency_df1, fig_currency1 = currency(currency_selected)
    cd1 = currency_df1["Close"].iloc[-1]
    cd2 = 1 / cd1
    c11, c12 = st.columns([5, 1])
    with c11:
        with st.expander("Get the data here!"):
            st.write(currency_df1)
    with c12:
        st.metric("Exchange Rate:", cd2.round(2))
    st.info(
        """
          Map Excange Rates across Currencies.
          The metric as presented above shows how much of the initial
          currency compensates for a unit of the following currency.
          """
    )
    st.plotly_chart(fig_currency1)
st.write("  --------  ")
df_vix, fig_vix = vix()
l_vix = df_vix.iloc[-1]
df_ivix, fig_ivix = ivix()
l_ivix = df_ivix.iloc[-1]
with st.container(border=True):
    cn1, cn2, cn3 = st.columns([3, 2, 1])
    with cn1:
        st.header("E. Market Volatility Index",  divider='rainbow')
    with cn2:
        st.write(" ")
        st.markdown(
            """Estimate Uncertainty Levels in the Markets to
        gauge your Risk Exposure"""
        )
    with cn3:
        st.metric("Market VIX", l_vix["Close"].round(2))
        st.metric("Market IVIX", l_ivix["Close"].round(2))
    st.plotly_chart(fig_vix, use_container_width=True)
    st.plotly_chart(fig_ivix, use_container_width=True)
st.write("  --------  ")
df_treasury, fig_treasury = treasury()
l_ustreasury = df_treasury["Close"].iloc[-1]


with st.container(border=True):
    bn1, bn2, bn3 = st.columns([3, 2, 1])
    with bn1:
        st.header("G. Treasury Yield Rates", divider='rainbow')
    with bn2:
        st.write(" ")
        st.markdown(
            """Estimate the real Risk-Free rate >> Yield of the
                Treasury bond - Inflation Rate"""
        )
    with bn3:
        st.write(" ")
        st.metric("US Treasury", l_ustreasury.round(2))

with st.container(border=True):
    tr1, tr2 = st.tabs(["US Treasury", "Reserve Bank of India"])
    with tr1:
        st.plotly_chart(fig_treasury, use_container_width=True)
    with tr2:
        st.write("We're working on this. Shall be up and about soon")

st.write("  --------  ")
c0, column1, column2, column3, column4, column5, c0a = st.columns([1, 1, 1, 1, 1, 1, 1])
with c0:
    st.write(" ")
with column1:
    st.image(ytube, "[Ledgr's YouTube Channel](%s)" % url_ytube, width=60)
with column2:
    st.image(fbook, "[Our Meta Page ](%s)" % url_fb, width=60)
with column3:
    st.image(linkedin, "[Ledgr @ LinkedIn](%s)" % url_linkedin, width=60)
with column4:
    st.write(" ")
    st.image(ledgrblog, "[Ledgr's Blog ](%s)" % url_blog, width=85)
    st.write(" ")
with column5:
    st.image(insta, "[Ledgr @ Insta](%s)" % url_insta, width=60)
with c0a:
    st.write(" ")
# # ###################################################################
with st.container():
    f9, f10, f11 = st.columns([2, 5, 1])
    with f9:
        st.write(" ")
    with f10:
        st.write(": 2025 - 2026 | All Rights Reserved  ©  Ledgr Inc.")
        st.write(": alphaLedgr.com | alphaLedgr Technologies Ltd. :")
    with f11:
        st.write(" ")
