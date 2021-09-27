from datetime import datetime

import pandas as pd
import streamlit as st

from API.fetch_data import request_ticker
from configuration import STOCKS
from optimization.stochastic_oscillator import stochastic_oscillator_optimization
from trading.ema_crossover import ema_crossover_strategy
from visualization.ema_crossover import plot_ema_crossover
from visualization.price import plot_price
from visualization.stochastic_oscillator_crossover import plot_stochastic_oscillator

st.set_page_config(layout="wide", page_title="Trading Strategy")


def render_sidebar() -> (str, str, str):
    st.sidebar.title(body="Configuration")
    ticker = st.sidebar.selectbox(label="Select symbol", options=STOCKS)
    now = datetime.now()
    start_date = st.sidebar.date_input(
        label="Start date:",
        value=datetime(2021, 3, 1),
        min_value=datetime(2015, 1, 1),
        max_value=now
    )
    end_date = st.sidebar.date_input(
        label="End date:",
        value=now,
        min_value=start_date,
        max_value=now
    )
    return ticker, start_date, end_date


def render_price(stock: pd.DataFrame, start_date: str, end_date: str):
    st.markdown("<h1 style='text-align: center;'>Price</h1>", unsafe_allow_html=True)
    fig = plot_price(stock=stock, start_date=start_date, end_date=end_date)
    st.pyplot(fig)


def render_ema_crossover(stock: pd.DataFrame, start_date: str, end_date: str):
    st.markdown("<h1 style='text-align: center;'>EMA Crossover</h1>",
                unsafe_allow_html=True)
    crossover = ema_crossover_strategy(stock=stock)
    fig = plot_ema_crossover(strategy=crossover, start_date=start_date, end_date=end_date)
    st.pyplot(fig)


def render_oscillator_crossover(stock: pd.DataFrame, start_date: str, end_date: str):
    st.markdown("<h1 style='text-align: center;'>Stochastic Oscillator</h1>",
                unsafe_allow_html=True)
    stochastic_oscillator = stochastic_oscillator_optimization(stock=stock)
    fig = plot_stochastic_oscillator(strategy=stochastic_oscillator,
                                     start_date=start_date, end_date=end_date)
    st.pyplot(fig)


def app():
    ticker, start_date, end_date = render_sidebar()
    stock = request_ticker(ticker_name=ticker)
    render_price(stock=stock, start_date=start_date, end_date=end_date)
    render_ema_crossover(stock=stock, start_date=start_date, end_date=end_date)
    render_oscillator_crossover(stock=stock, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    app()
