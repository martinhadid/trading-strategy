import pandas as pd

from utils import moving_diff, moving_average

PERIODS = 14


def _wilder_smoothing(values: pd.Series, initial_avg: float, name: str) -> pd.Series:
    # https://blog.quantinsti.com/rsi-indicator/
    avg_values = [None] * PERIODS
    avg_values.append(initial_avg)

    for _, value in values[PERIODS + 1:].items():
        avg = (initial_avg * (PERIODS - 1) + value) / PERIODS
        avg_values.append(avg)
        initial_avg = avg

    return pd.Series(data=avg_values, index=values.index, name=name)


def relative_strength_index(stock: pd.DataFrame) -> pd.Series:
    change = moving_diff(price=stock["Close"], days=1, name="change")
    gain = pd.Series(data=change.clip(lower=0), name="gain")
    loss = pd.Series(data=abs(change.clip(upper=0)), name="loss")
    assert all(gain.index == loss.index)

    init_avg_gain = moving_average(
        price=gain,
        days=PERIODS,
        min_periods=PERIODS,
        name="average_gain"
    ).iloc[PERIODS]
    init_avg_loss = moving_average(
        price=loss,
        days=PERIODS,
        min_periods=PERIODS,
        name="average_loss"
    ).iloc[PERIODS]

    wilder_smoothing_avg_gain = _wilder_smoothing(
        values=gain,
        initial_avg=init_avg_gain,
        name="avg_gain"
    )
    wilder_smoothing_avg_loss = _wilder_smoothing(
        values=loss,
        initial_avg=init_avg_loss,
        name="avg_loss"
    )

    rs = wilder_smoothing_avg_gain / wilder_smoothing_avg_loss
    return pd.Series(data=100 - (100 / (1 + rs)), name="rsi")


if __name__ == "__main__":
    df = pd.read_csv('../test/rsi.csv')
    print(relative_strength_index(df))
