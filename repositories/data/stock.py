from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class Stock:
    price: pd.Series

    def simple_moving_average(self, periods: int, name: str) -> pd.Series:
        sma = self.price.rolling(window=periods, min_periods=1).mean()
        return sma.rename(name)

    def exponential_moving_average(self, days: int, name: str) -> pd.Series:
        ema = self.price.ewm(span=days, adjust=False).mean()
        return ema.rename(name)

    def moving_max(self, periods: int, name: str) -> pd.Series:
        moving_max = self.price.rolling(window=periods, min_periods=1).max()
        return moving_max.rename(name)

    def moving_min(self, periods: int, name: str) -> pd.Series:
        moving_min = self.price.rolling(window=periods, min_periods=1).min()
        return moving_min.rename(name)
