import numpy as np
import pandas as pd

from utils.ewm import (price_moving_average_10_days,
                       price_moving_average_20_days)


def _generate_signals_from_crossovers(df: pd.DataFrame) -> pd.DataFrame:
    df["signal"] = 0
    df["signal"] = np.where(df["SMA_10"] > df["SMA_20"], 1, 0)
    return df


def _set_position(df: pd.DataFrame) -> pd.DataFrame:
    df["position"] = df["signal"].diff()
    return df


def _set_stop_loss(df: pd.DataFrame) -> pd.DataFrame:
    return df


def set_trading_strategy(df: pd.DataFrame):
    df["SMA_10"] = price_moving_average_10_days(df)
    df["SMA_20"] = price_moving_average_20_days(df)
    df_stock_signals = _generate_signals_from_crossovers(df=df)
    return _set_position(df=df_stock_signals)
    # return _set_stop_loss(df_stock_position=df_stock_position)
