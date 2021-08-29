import numpy as np
import pandas as pd

from utils.sma import price_moving_average_10_days, price_moving_average_20_days


def _generate_signals_from_crossovers(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["signal"] = 0
    df_signals["signal"] = np.where(df_signals["SMA_10"] > df_signals["SMA_20"], 1, 0)
    return df_signals


def _set_position(df_signals: pd.DataFrame) -> pd.DataFrame:
    df_signals["position"] = df_signals["signal"].diff()
    return df_signals


def _set_stop_loss(df_stock_position: pd.DataFrame) -> pd.DataFrame:
    return df_stock_position


def set_trading_strategy(df_stock: pd.DataFrame):
    df_stock["SMA_10"] = price_moving_average_10_days(df_stock)
    df_stock["SMA_20"] = price_moving_average_20_days(df_stock)
    df_stock_signals = _generate_signals_from_crossovers(df_signals=df_stock)
    return _set_position(df_signals=df_stock_signals)
    # return _set_stop_loss(df_stock_position=df_stock_position)
