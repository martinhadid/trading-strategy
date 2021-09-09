import pandas as pd
import streamlit as st
import yfinance as yf

from configuration import STOCKS, VALID_PERIODS
from trading.sma_crossover_strategy import set_trading_strategy
from trading.tendency import stock_tendency
from visualization.sma_crossover_signals import plot_sma_signals

st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="Trading Stategy",
    page_icon=None,
)


def request_ticker_prices(ticker_name: str, period: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_name)
    df_ticker = ticker.history(period=period)
    return df_ticker.loc[:, ["Open", "Low", "High", "Close"]]


def render_sidebar() -> (str, str):
    st.sidebar.title(body="Configuration")
    ticker = st.sidebar.selectbox(label="Select one symbol", options=STOCKS)
    period = st.sidebar.selectbox(label="Select Period", options=("6mo", *VALID_PERIODS))
    return ticker, period


def render_sma_signals(chart_data: pd.DataFrame):
    st.markdown("<h1 style='text-align: center;'>Simple Moving Average Crossover</h1>",
                unsafe_allow_html=True)
    fig = plot_sma_signals(df=chart_data)
    st.pyplot(fig)


def app():
    ticker, period = render_sidebar()
    stock_data = request_ticker_prices(ticker_name=ticker, period=period)
    df_stock = stock_tendency(df_stock=stock_data)
    df_stock_position = set_trading_strategy(df_stock=df_stock)
    render_sma_signals(chart_data=df_stock_position)


if __name__ == "__main__":
    app()
