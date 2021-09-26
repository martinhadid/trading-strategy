import numpy as np
import pandas as pd

from repositories.data.signal import Signal
from repositories.data.stock import Stock


def ema_crossover(stock: Stock) -> Signal:
    ema_10 = stock.exponential_moving_average(days=10, name="ema_10")
    ema_20 = stock.exponential_moving_average(days=20, name="ema_20")

    assert all(ema_10.index == ema_20.index)

    return Signal(
        ema_10=ema_10,
        ema_20=ema_20,
        crossover=pd.Series(
            data=np.where(ema_10 > ema_20, 1, 0),
            index=ema_10.index
        ).diff()
    )
