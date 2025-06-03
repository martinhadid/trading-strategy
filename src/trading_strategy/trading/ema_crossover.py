"""Trading strategy for ema crossover."""

import pandas as pd

from trading_strategy.utils import crossover
from trading_strategy.utils import exponential_moving_average


def ema_crossover(stock: pd.DataFrame) -> pd.DataFrame:
    """Calculates an EMA crossover trading strategy for a given stock DataFrame.

    This function computes 10-day and 20-day Exponential Moving Averages (EMAs)
    of the 'Close' price and then generates a crossover signal.

    Args:
        stock (pd.DataFrame): A DataFrame containing stock data, expected to have a 'Close' column.

    Returns:
        pd.DataFrame: A DataFrame containing the 'ema_10' series, 'ema_20' series,
                      and a 'crossover' signal series (1 for buy, -1 for sell, 0 otherwise).
    """
    close_price = stock["Close"]
    ema_10 = exponential_moving_average(price=close_price, days=10, name="ema_10")
    ema_20 = exponential_moving_average(price=close_price, days=20, name="ema_20")
    return crossover(fast=ema_10, slow=ema_20)
