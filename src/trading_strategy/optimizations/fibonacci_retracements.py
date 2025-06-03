"""Fibonacci retracements optimization."""

import pandas as pd

from trading_strategy.trading.ema_crossover import ema_crossover


def fibonacci_retracements_optimization(stock: pd.DataFrame) -> pd.DataFrame:
    """Combines stock closing prices with EMA crossover signals for potential Fibonacci retracements analysis.

    This function calculates the EMA crossover strategy signals and concatenates them
    with the stock's closing prices into a single DataFrame. This combined output
    can then be used as input for further analysis involving Fibonacci retracements.

    Args:
        stock (pd.DataFrame): A DataFrame containing stock data, expected to have a 'Close' column
                              and sufficient data for EMA crossover calculation.

    Returns:
        pd.DataFrame: A DataFrame containing the stock's 'Close' price,
                      the 'ema_10', 'ema_20', and 'crossover' series from the EMA crossover strategy.
    """
    ema_crossover_df = ema_crossover(stock=stock)
    close_price = stock["Close"]
    return pd.concat([close_price, ema_crossover_df], axis=1)
