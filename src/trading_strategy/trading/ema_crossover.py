import pandas as pd

from trading_strategy.utils import crossover
from trading_strategy.utils import exponential_moving_average


def ema_crossover(stock: pd.DataFrame) -> pd.DataFrame:
    close_price = stock["Close"]
    ema_10 = exponential_moving_average(price=close_price, days=10, name="ema_10")
    ema_20 = exponential_moving_average(price=close_price, days=20, name="ema_20")
    return crossover(fast=ema_10, slow=ema_20)
