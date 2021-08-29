from functools import partial

import numpy as np
import pandas as pd


def _ticker_close_price(df_ticker: pd.DataFrame) -> pd.DataFrame:
    return df_ticker.loc[:, ["Open", "Low", "High", "Close"]]


def _price_moving_average(days: int, df_ticker: pd.DataFrame) -> pd.Series:
    return df_ticker["Close"].rolling(window=days, min_periods=1).mean()


_price_moving_average_10_days = partial(_price_moving_average, 10)
_price_moving_average_20_days = partial(_price_moving_average, 20)


def _generate_signals_from_crossovers(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["signal"] = 0
    df_signals["signal"] = np.where(df_signals["SMA_10"] > df_signals["SMA_20"], 1, 0)
    return df_signals


def _set_position(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["position"] = df_signals["signal"].diff()
    return df_signals


def set_trading_strategy(ticker: pd.DataFrame):
    df_stock = _ticker_close_price(df_ticker=ticker)
    df_stock["SMA_10"] = _price_moving_average_10_days(df_stock)
    df_stock["SMA_20"] = _price_moving_average_20_days(df_stock)
    df_stock_signals = _generate_signals_from_crossovers(df_signals=df_stock)
    return _set_position(df_signals=df_stock_signals)
