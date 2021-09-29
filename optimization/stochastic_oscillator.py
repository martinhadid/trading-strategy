import pandas as pd

from utils import (moving_max, moving_min, moving_sum, exponential_moving_average,
                   crossover)

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


def stochastic_oscillator_optimization(stock: pd.DataFrame) -> pd.DataFrame:
    close_price = stock["Close"]
    high_price = stock["High"]
    low_price = stock["Low"]

    k_high = moving_max(price=high_price, days=K_TIME_PERIODS, name="sma_14_high")
    k_low = moving_min(price=low_price, days=K_TIME_PERIODS, name="sma_14_low")

    price_low_diff_sum = moving_sum(
        price=close_price - k_low,
        days=K_SLOWING_PERIODS,
        name="price_low_diff_sum"
    )
    high_low_diff_sum = moving_sum(
        price=k_high - k_low,
        days=K_SLOWING_PERIODS,
        name="high_low_diff_sum"
    )

    k = pd.Series(data=100 * price_low_diff_sum / high_low_diff_sum, name="k")
    d = exponential_moving_average(price=k, days=D_TIME_PERIODS, name="d")
    assert all(k.index == d.index)

    return crossover(fast=k, slow=d)
