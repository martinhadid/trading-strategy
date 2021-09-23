import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

from utils.plots import get_x_axis_dates, X_ROTATION, FIG_SIZE, ARROW_SIZE


def plot_ewm_signals(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    # ax.plot(df.index, df["Close"])
    ax.plot(df.index, df["SMA_10"])
    ax.plot(df.index, df["SMA_20"])

    open_position = df[df["position"] == 1]["SMA_10"]
    ax.scatter(open_position.index, open_position, marker="^", s=ARROW_SIZE, color="g")

    close_position = df[df["position"] == -1]["SMA_10"]
    ax.scatter(close_position.index, close_position, marker="v", s=ARROW_SIZE, color="r")

    x_axis_dates = get_x_axis_dates(
        df_dates=df.index,
        open_dates=open_position.index,
        close_dates=close_position.index,
    )
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["SMA_10", "SMA_20", "Buy", "Sell"])
    ax.grid()
    return fig
