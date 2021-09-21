import pandas as pd
import streamlit as st
import yfinance as yf

from configuration import STOCKS, VALID_PERIODS
from optimization.stochastic_oscillator import stochastic_oscillator
from trading.ewm_crossover_strategy import set_trading_strategy
from trading.tendency import stock_tendency
from visualization.ewm_crossover_signals import plot_ewm_signals
from visualization.stochastic_oscillator_signals import plot_stochastic_oscillator_signals

st.set_page_config(
    layout="wide", initial_sidebar_state="auto", page_title="Trading Stategy",
    page_icon=None
)


def request_ticker_prices(ticker_name: str, period: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_name)
    df = ticker.history(period=period)
    return df.loc[:, ["Open", "Low", "High", "Close", "Volume"]]


def render_sidebar() -> (str, str):
    st.sidebar.title(body="Configuration")
    ticker = st.sidebar.selectbox(label="Select one symbol", options=STOCKS)
    period = st.sidebar.selectbox(label="Select Period", options=("6mo", *VALID_PERIODS))
    return ticker, period


def render_ewm_signals(chart_data: pd.DataFrame):
    fig = plot_ewm_signals(df=chart_data)
    st.pyplot(fig)


def render_stochastic_oscillator(chart_data: pd.DataFrame):
    fig = plot_stochastic_oscillator_signals(df=chart_data)
    st.pyplot(fig)


def app():
    ticker, period = render_sidebar()
    stock_data = request_ticker_prices(ticker_name=ticker, period=period)
    df_stock = stock_tendency(df=stock_data)
    df_stock_position = set_trading_strategy(df=df_stock)
    df_stochastic_oscillator = stochastic_oscillator(df=df_stock_position)

    render_ewm_signals(chart_data=df_stock_position)
    render_stochastic_oscillator(chart_data=df_stochastic_oscillator)


if __name__ == "__main__":
    app()
