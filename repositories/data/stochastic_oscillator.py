from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class StochasticOscillator:
    k: pd.Series
    d: pd.Series
    crossover: pd.Series
