import pandas as pd

from trading.ema_crossover import ema_crossover_strategy


def fibonacci_retracements_optimization(stock: pd.DataFrame) -> pd.DataFrame:
    ema_crossover = ema_crossover_strategy(stock=stock)
    close_price = stock["Close"]
    return pd.concat([close_price, ema_crossover], axis=1)
