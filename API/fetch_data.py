import pandas as pd
import streamlit as st
import yfinance as yf

PERIOD = "5y"
INTERVAL = "1d"


@st.cache_data
def request_ticker(ticker_name: str) -> pd.DataFrame:
    return yf.download(tickers=ticker_name, period=PERIOD, interval=INTERVAL)
