import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

FIG_SIZE = (20, 10)
X_ROTATION = 90
VALUE_OFFSET = (5, 25)
ARROW_SIZE = 150


def _get_x_axis_dates(df_dates: pd.Index, open_dates: pd.DatetimeIndex,
                      close_dates: pd.DatetimeIndex) -> pd.DatetimeIndex:
    start_days = pd.date_range(start=df_dates[0], end=df_dates[-1], freq="MS")
    return open_dates.union(close_dates).union(start_days)


def plot_ewm_signals(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # ax.plot(df.index, df["Close"])
    ax.plot(df.index, df["SMA_10"])
    ax.plot(df.index, df["SMA_20"])
    ax.plot(df.index, df["SMA_100"])

    open_position = df[df["position"] == 1]["SMA_10"]
    ax.scatter(open_position.index, open_position, marker="^", s=ARROW_SIZE, color="g")
    for index, value in open_position.iteritems():
        ax.annotate(
            text=round(value),
            xy=(index, value),
            xytext=VALUE_OFFSET,
            textcoords="offset points",
            ha="center",
        )

    close_position = df[df["position"] == -1]["SMA_10"]
    ax.scatter(close_position.index, close_position, marker="v", s=ARROW_SIZE, color="r")

    for index, value in close_position.iteritems():
        ax.annotate(
            text=round(value),
            xy=(index, value),
            xytext=VALUE_OFFSET,
            textcoords="offset points",
            ha="center",
        )

    x_axis_dates = _get_x_axis_dates(
        df_dates=df.index,
        open_dates=open_position.index,
        close_dates=close_position.index,
    )
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["SMA_10", "SMA_20", "SMA_100", "Buy", "Sell"])
    ax.set(xlabel="Date", ylabel="Close Price")
    ax.grid()
    return fig
