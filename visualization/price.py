import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from utils.plots import get_x_axis_dates, FIG_SIZE, VALUE_OFFSET, X_ROTATION, \
    ARROW_SIZE


def plot_price(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(df["Close"])
    ax.plot(df.index, df["SMA_100"])

    open_position = df[df["position"] == 1]["Close"]
    ax.scatter(open_position.index, open_position, marker=".", s=ARROW_SIZE, color="g")
    for index, value in open_position.iteritems():
        ax.annotate(
            text=round(value, 2),
            xy=(index, value),
            xytext=VALUE_OFFSET,
            textcoords="offset points",
            ha="center",
        )

    close_position = df[df["position"] == -1]["Close"]
    ax.scatter(close_position.index, close_position, marker=".", s=ARROW_SIZE, color="r")
    for index, value in close_position.iteritems():
        ax.annotate(
            text=round(value, 2),
            xy=(index, value),
            xytext=VALUE_OFFSET,
            textcoords="offset points",
            ha="center",
        )

    x_axis_dates = get_x_axis_dates(
        df_dates=df.index,
        open_dates=open_position.index,
        close_dates=close_position.index,
    )
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["Close Price", "SMA_100"])
    ax.grid()
    return fig
