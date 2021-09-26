from dataclasses import dataclass

import pandas as pd


@dataclass
class Signal:
    ema_10: pd.Series
    ema_20: pd.Series
    crossover: pd.Series
