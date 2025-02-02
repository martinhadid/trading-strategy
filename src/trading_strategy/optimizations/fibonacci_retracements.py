import pandas as pd

from trading_strategy.trading.ema_crossover import ema_crossover


def fibonacci_retracements_optimization(stock: pd.DataFrame) -> pd.DataFrame:
    ema_crossover = ema_crossover(stock=stock)
    close_price = stock["Close"]
    return pd.concat([close_price, ema_crossover], axis=1)
