import pandas as pd

from utils.sma import price_moving_average_100_days


def stock_tendency(df_stock: pd.DataFrame):
    df_stock["SMA_100"] = price_moving_average_100_days(df_stock)
    return df_stock
