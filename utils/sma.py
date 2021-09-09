from functools import partial

import pandas as pd


def _price_moving_average(days: int, df: pd.DataFrame) -> pd.Series:
    return df["Close"].rolling(window=days).mean()


price_moving_average_10_days = partial(_price_moving_average, 10)
price_moving_average_20_days = partial(_price_moving_average, 20)
price_moving_average_100_days = partial(_price_moving_average, 100)
