import pandas as pd

from utils.ewm import price_moving_average_100_days


def stock_tendency(df: pd.DataFrame):
    df["SMA_100"] = price_moving_average_100_days(df)
    return df
