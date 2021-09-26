import numpy as np
import pandas as pd

from repositories.data.stochastic_oscillator import StochasticOscillator
from repositories.data.stock import Stock

"""
https://www.metastock.com/customer/resources/taaz/?p=106
https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/slow-stochastic
Calculation
Slow %K= 100[Sum of the (C - L14) for the %K Slowing Period / Sum of the (H14 – L14) for the %K Slowing Period]
Slow %D = EMA of Slow %K
Where:
C = Latest Close
L14 = Lowest low for the last 14 periods
H14 = Highest high for the same 14 periods
%K Slowing Period = 6
"""

K_TIME_PERIODS = 14
K_SLOWING_PERIODS = 6
D_TIME_PERIODS = 3


def stochastic_oscillator_optimization(stock_close: Stock, stock_high: Stock,
                                       stock_low: Stock) -> StochasticOscillator:
    k_high = stock_high.moving_max(periods=K_TIME_PERIODS, name="sma_14_high")
    k_low = stock_low.moving_min(periods=K_TIME_PERIODS, name="sma_14_low")

    price_low_difference = stock_close.price - k_low
    high_low_difference = k_high - k_low

    price_low_diff_sum = price_low_difference.rolling(window=K_SLOWING_PERIODS).sum()
    high_low_diff_sum = high_low_difference.rolling(window=K_SLOWING_PERIODS).sum()

    k = 100 * price_low_diff_sum / high_low_diff_sum
    d = k.ewm(span=D_TIME_PERIODS, adjust=False).mean()

    assert all(k.index == d.index)

    return StochasticOscillator(
        k=k,
        d=d,
        crossover=pd.Series(
            data=np.where(k > d, 1, 0),
            index=k.index
        ).diff()
    )
