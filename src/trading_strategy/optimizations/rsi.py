"""Relative strength index module."""

import pandas as pd

from trading_strategy.config import config_parser
from trading_strategy.utils import moving_average
from trading_strategy.utils import moving_diff

config = config_parser.parse_from_file(config_file="config.toml")
PERIODS = config.optimizations.rsi.period


def _wilder_smoothing(values: pd.Series, initial_avg: float, name: str) -> pd.Series:
    """Applies Wilder's smoothing method to a series of values.

    This is a specific type of exponential moving average commonly used in RSI calculation.

    Args:
        values (pd.Series): The input series to be smoothed.
        initial_avg (float): The initial average value for the smoothing calculation.
        name (str): The name to assign to the resulting smoothed series.

    Returns:
        pd.Series: A series containing the Wilder-smoothed values.
    """
    # https://blog.quantinsti.com/rsi-indicator/
    avg_values = [None] * PERIODS
    avg_values.append(initial_avg)

    for _, value in values[PERIODS + 1 :].items():
        avg = (initial_avg * (PERIODS - 1) + value) / PERIODS
        avg_values.append(avg)
        initial_avg = avg

    return pd.Series(data=avg_values, index=values.index, name=name)


def relative_strength_index(stock: pd.DataFrame) -> pd.Series:
    """Calculates the Relative Strength Index (RSI) for a given stock DataFrame.

    The RSI is a momentum indicator that measures the magnitude of recent price
    changes to evaluate overbought or oversold conditions in the price of a stock
    or other asset.

    Args:
        stock (pd.DataFrame): A DataFrame containing stock data, expected to have a 'Close' column.

    Returns:
        pd.Series: A series representing the Relative Strength Index (RSI) values.
    """
    change = moving_diff(price=stock["Close"], days=1, name="change")
    gain = pd.Series(data=change.clip(lower=0), name="gain")
    loss = pd.Series(data=abs(change.clip(upper=0)), name="loss")
    assert all(gain.index == loss.index)

    init_avg_gain = moving_average(
        price=gain, days=PERIODS, min_periods=PERIODS, name="average_gain"
    ).iloc[PERIODS]
    init_avg_loss = moving_average(
        price=loss, days=PERIODS, min_periods=PERIODS, name="average_loss"
    ).iloc[PERIODS]

    wilder_smoothing_avg_gain = _wilder_smoothing(
        values=gain, initial_avg=init_avg_gain, name="avg_gain"
    )
    wilder_smoothing_avg_loss = _wilder_smoothing(
        values=loss, initial_avg=init_avg_loss, name="avg_loss"
    )

    rs = wilder_smoothing_avg_gain / wilder_smoothing_avg_loss
    return pd.Series(data=100 - (100 / (1 + rs)), name="rsi")
