import pandas as pd

X_ROTATION = 90
VALUE_OFFSET = (5, 25)
FIG_SIZE = (20, 5)
ARROW_SIZE = 150


def get_x_axis_dates(df_dates: pd.Index, open_dates: pd.DatetimeIndex,
                     close_dates: pd.DatetimeIndex) -> pd.DatetimeIndex:
    start_days = pd.date_range(start=df_dates[0], end=df_dates[-1], freq="MS")
    return open_dates.union(close_dates).union(start_days)
