"""Module to download ticker data."""

import pandas as pd
import streamlit as st
import yfinance as yf

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


@st.cache_data
def request_ticker(ticker_name: str) -> pd.DataFrame:
    """Download ticker data."""
    return yf.download(
        tickers=ticker_name,
        period=config.data.period,
        multi_level_index=False,
    )
