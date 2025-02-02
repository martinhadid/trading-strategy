"""Main app."""

from datetime import datetime

from matplotlib.figure import Figure
import streamlit as st

from trading_strategy.API import fetch_data
from trading_strategy.optimizations.rsi import relative_strength_index
from trading_strategy.optimizations.stochastic_oscillator import stochastic_oscillator
from trading_strategy.plots.ema_crossover import plot_ema
from trading_strategy.plots.price import plot_price
from trading_strategy.plots.rsi import plot_rsi
from trading_strategy.plots.stochastic_oscillator_crossover import (
    plot_stochastic_oscillator,
)
from trading_strategy.trading.ema_crossover import ema_crossover

st.set_page_config(layout="wide", page_title="Trading Strategy")


def _render_sidebar() -> tuple[str, str, str]:
    st.sidebar.title("Configuration")
    ticker = st.sidebar.text_input("Select symbol", "QQQ")
    now = datetime.now()
    start_date = st.sidebar.date_input(
        label="Start date:",
        value=datetime(2024, 3, 1),
        min_value=datetime(2015, 1, 1),
        max_value=now,
    )
    end_date = st.sidebar.date_input(
        label="End date:", value=now, min_value=start_date, max_value=now
    )
    return ticker, start_date, end_date


def _render_section(title: str, fig: Figure) -> None:
    """Renders a section with a title and plot."""
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
    st.pyplot(fig)


def main():
    """App entrypoint."""
    ticker, start_date, end_date = _render_sidebar()
    stock = fetch_data.request_ticker(ticker_name=ticker)
    price_fig = plot_price(stock, start_date, end_date)
    _render_section("Price", price_fig)
    ema_fig = plot_ema(ema_crossover(stock), start_date, end_date)
    _render_section("EMA Crossover", ema_fig)
    stochastic_oscillator_fig = plot_stochastic_oscillator(
        stochastic_oscillator(stock), start_date, end_date
    )
    _render_section("Stochastic Oscillator", stochastic_oscillator_fig)
    rsi_fig = plot_rsi(relative_strength_index(stock), start_date, end_date)
    _render_section("RSI", rsi_fig)


if __name__ == "__main__":
    main()
