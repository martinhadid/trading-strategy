"""Math calculations."""

import numpy as np
import pandas as pd


def moving_diff(price: pd.Series, days: int, name: str) -> pd.Series:
    """Calculates the moving difference of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the difference calculation.
        name (str): The name to assign to the resulting series.

    Returns:
        pd.Series: A series representing the moving difference.
    """
    diff = price.diff(periods=days)
    return diff.rename(name)


def moving_sum(
    price: pd.Series, days: int, name: str, min_periods: int = 1
) -> pd.Series:
    """Calculates the moving sum of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the rolling window.
        name (str): The name to assign to the resulting series.
        min_periods (int, optional): Minimum number of observations in window required
            to have a value. Defaults to 1.

    Returns:
        pd.Series: A series representing the moving sum.
    """
    sma = price.rolling(window=days, min_periods=min_periods).sum()
    return sma.rename(name)


def moving_average(
    price: pd.Series, days: int, name: str, min_periods: int = 1
) -> pd.Series:
    """Calculates the simple moving average (SMA) of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the rolling window.
        name (str): The name to assign to the resulting series.
        min_periods (int, optional): Minimum number of observations in window required
            to have a value. Defaults to 1.

    Returns:
        pd.Series: A series representing the simple moving average.
    """
    sma = price.rolling(window=days, min_periods=min_periods).mean()
    return sma.rename(name)


def exponential_moving_average(price: pd.Series, days: int, name: str) -> pd.Series:
    """Calculates the exponential moving average (EMA) of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the EMA calculation (span).
        name (str): The name to assign to the resulting series.

    Returns:
        pd.Series: A series representing the exponential moving average.
    """
    ema = price.ewm(span=days, adjust=False).mean()
    return ema.rename(name)


def moving_max(
    price: pd.Series, days: int, name: str, min_periods: int = 1
) -> pd.Series:
    """Calculates the moving maximum of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the rolling window.
        name (str): The name to assign to the resulting series.
        min_periods (int, optional): Minimum number of observations in window required
            to have a value. Defaults to 1.

    Returns:
        pd.Series: A series representing the moving maximum.
    """
    rolling_max = price.rolling(window=days, min_periods=min_periods).max()
    return rolling_max.rename(name)


def moving_min(
    price: pd.Series, days: int, name: str, min_periods: int = 1
) -> pd.Series:
    """Calculates the moving minimum of a price series.

    Args:
        price (pd.Series): The input price series.
        days (int): The number of periods for the rolling window.
        name (str): The name to assign to the resulting series.
        min_periods (int, optional): Minimum number of observations in window required
            to have a value. Defaults to 1.

    Returns:
        pd.Series: A series representing the moving minimum.
    """
    rolling_min = price.rolling(window=days, min_periods=min_periods).min()
    return rolling_min.rename(name)


def crossover(fast: pd.Series, slow: pd.Series) -> pd.DataFrame:
    """Calculates a crossover between two series and returns the series with the signal.

    Args:
        fast (pd.Series): The "fast" series (e.g., faster moving average).
        slow (pd.Series): The "slow" series (e.g., slower moving average).

    Returns:
        pd.DataFrame: A DataFrame containing the fast series, slow series, and the crossover signal.
            The signal is 1 when fast crosses above slow, -1 when fast crosses below slow, and 0 otherwise.
    """
    assert all(fast.index == slow.index)
    strategy = pd.Series(
        data=np.where(fast > slow, 1, 0),
        index=fast.index,
        name="crossover",
    ).diff()
    return pd.concat([fast, slow, strategy], axis=1)
