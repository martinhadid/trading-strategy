import pandas as pd

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


def stochastic_oscillator(df: pd.DataFrame) -> pd.DataFrame:
    df["K_High"] = df["High"].rolling(
        window=K_TIME_PERIODS,
        min_periods=K_TIME_PERIODS
    ).max()

    df["K_Low"] = df["Low"].rolling(
        window=K_TIME_PERIODS,
        min_periods=K_TIME_PERIODS
    ).min()

    price_low_difference = df["Close"] - df["K_Low"]
    high_low_difference = df["K_High"] - df["K_Low"]

    price_low_difference_sum = price_low_difference.rolling(
        window=K_SLOWING_PERIODS,
        min_periods=K_SLOWING_PERIODS
    ).sum()

    high_low_difference_sum = high_low_difference.rolling(
        window=K_SLOWING_PERIODS,
        min_periods=K_SLOWING_PERIODS
    ).sum()

    df["%K"] = 100 * price_low_difference_sum / high_low_difference_sum
    df["%D"] = df["%K"].ewm(span=D_TIME_PERIODS, adjust=False).mean()
    return df
