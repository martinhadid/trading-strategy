import pandas as pd

from trading_strategy.config import config_parser
from trading_strategy.utils import crossover
from trading_strategy.utils import exponential_moving_average
from trading_strategy.utils import moving_max
from trading_strategy.utils import moving_min
from trading_strategy.utils import moving_sum

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


config = config_parser.parse_from_file(config_file="config.toml")
K_TIME_PERIODS = config.optimizations.stochastic_oscillator.k_time_periods
K_SLOWING_PERIODS = config.optimizations.stochastic_oscillator.k_slowing_periods
D_TIME_PERIODS = config.optimizations.stochastic_oscillator.d_time_periods


def stochastic_oscillator(stock: pd.DataFrame) -> pd.DataFrame:
    close_price = stock["Close"]
    high_price = stock["High"]
    low_price = stock["Low"]
    k_high = moving_max(price=high_price, days=K_TIME_PERIODS, name="sma_14_high")
    k_low = moving_min(price=low_price, days=K_TIME_PERIODS, name="sma_14_low")
    price_low_diff_sum = moving_sum(
        price=close_price - k_low,
        days=K_SLOWING_PERIODS,
        name="price_low_diff_sum",
    )
    high_low_diff_sum = moving_sum(
        price=k_high - k_low,
        days=K_SLOWING_PERIODS,
        name="high_low_diff_sum",
    )
    k = pd.Series(data=100 * price_low_diff_sum / high_low_diff_sum, name="k")
    d = exponential_moving_average(price=k, days=D_TIME_PERIODS, name="d")
    assert all(k.index == d.index)
    return crossover(fast=k, slow=d)
