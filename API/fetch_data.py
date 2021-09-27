import pandas as pd
import yfinance as yf

PERIOD = "5y"
INTERVAL = "1d"


def request_ticker(ticker_name: str) -> pd.DataFrame:
    return yf.download(tickers=ticker_name, period=PERIOD, interval=INTERVAL)
