from datetime import datetime

import pandas as pd
import streamlit as st
import yfinance as yf

from configuration import STOCKS
from optimization.stochastic_oscillator import stochastic_oscillator
from trading.ewm_crossover_strategy import set_trading_strategy
from trading.tendency import stock_tendency
from visualization.ewm_crossover_signals import plot_ewm_signals
from visualization.price import plot_price
from visualization.stochastic_oscillator_signals import plot_stochastic_oscillator_signals

st.set_page_config(layout="wide", initial_sidebar_state="auto",
                   page_title="Trading Stategy")


@st.cache(allow_output_mutation=True)
def request_ticker(ticker_name: str) -> pd.DataFrame:
    return yf.download(tickers=ticker_name, period="5y", interval="1d")


def render_sidebar() -> (str, str, str):
    st.sidebar.title(body="Configuration")
    ticker = st.sidebar.selectbox(label="Select one symbol", options=STOCKS)
    start_date = st.sidebar.date_input(label="Start date:", value=datetime(2021, 3, 20))
    end_date = st.sidebar.date_input(label="End date:", value=datetime(2021, 9, 20))
    return ticker, start_date, end_date


def render_price(chart_data: pd.DataFrame):
    st.markdown("<h1 style='text-align: center;'>Close Price</h1>",
                unsafe_allow_html=True)
    fig = plot_price(df=chart_data)
    st.pyplot(fig)


def render_ewm_signals(chart_data: pd.DataFrame):
    st.markdown("<h1 style='text-align: center;'>EMA Crossover</h1>",
                unsafe_allow_html=True)
    fig = plot_ewm_signals(df=chart_data)
    st.pyplot(fig)


def render_stochastic_oscillator(chart_data: pd.DataFrame):
    st.markdown("<h1 style='text-align: center;'>Stochastic Oscillator</h1>",
                unsafe_allow_html=True)
    fig = plot_stochastic_oscillator_signals(df=chart_data)
    st.pyplot(fig)


def app():
    ticker, start_date, end_date = render_sidebar()
    stock_data = request_ticker(ticker_name=ticker)

    df_stock = stock_tendency(df=stock_data)
    df_stock_position = set_trading_strategy(df=df_stock)
    df_stochastic_oscillator = stochastic_oscillator(df=df_stock_position)

    chart_data = df_stochastic_oscillator.loc[start_date:end_date]
    render_price(chart_data=chart_data)
    render_ewm_signals(chart_data=chart_data)
    render_stochastic_oscillator(chart_data=chart_data)


if __name__ == "__main__":
    app()
