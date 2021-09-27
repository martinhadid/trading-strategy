import numpy as np
import pandas as pd


def moving_sum(price: pd.Series, days: int, name: str) -> pd.Series:
    sma = price.rolling(window=days, min_periods=1).sum()
    return sma.rename(name)


def moving_average(price: pd.Series, days: int, name: str) -> pd.Series:
    sma = price.rolling(window=days, min_periods=1).mean()
    return sma.rename(name)


def exponential_moving_average(price: pd.Series, days: int, name: str) -> pd.Series:
    ema = price.ewm(span=days, adjust=False).mean()
    return ema.rename(name)


def moving_max(price: pd.Series, days: int, name: str) -> pd.Series:
    moving_max = price.rolling(window=days, min_periods=1).max()
    return moving_max.rename(name)


def moving_min(price: pd.Series, days: int, name: str) -> pd.Series:
    moving_min = price.rolling(window=days, min_periods=1).min()
    return moving_min.rename(name)


def crossover(fast: pd.Series, slow: pd.Series) -> pd.DataFrame:
    assert all(fast.index == slow.index)
    strategy = pd.Series(
        data=np.where(fast > slow, 1, 0),
        index=fast.index,
        name="crossover"
    ).diff()
    return pd.concat([fast, slow, strategy], axis=1)
