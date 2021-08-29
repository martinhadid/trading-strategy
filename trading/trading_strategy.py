from functools import partial

import numpy as np
import pandas as pd
import yfinance as yf


def request_ticker(ticker_name: str, period: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_name)
    return ticker.history(period=period)


def ticker_close_price(df_ticker: pd.DataFrame) -> pd.DataFrame:
    return df_ticker.loc[:, ["Open", "Low", "High", "Close"]]


def price_moving_average(days: int, df_ticker: pd.DataFrame) -> pd.Series:
    return df_ticker["Close"].rolling(window=days, min_periods=1).mean()


price_moving_average_10_days = partial(price_moving_average, 10)
price_moving_average_20_days = partial(price_moving_average, 20)


def generate_signals_from_crossovers(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["signal"] = 0
    df_signals["signal"] = np.where(df_signals["SMA_10"] > df_signals["SMA_20"], 1, 0)
    return df_signals


def set_position(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["position"] = df_signals["signal"].diff()
    return df_signals
