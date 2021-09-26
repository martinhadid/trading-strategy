import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure

from repositories.data.signal import Signal
from visualization.settings import X_ROTATION, FIG_SIZE, ARROW_SIZE


def plot_ema_crossover(signal: Signal, start_date: str, end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ema_10 = signal.ema_10.loc[start_date:end_date]
    ema_20 = signal.ema_20.loc[start_date:end_date]
    ax.plot(ema_10)
    ax.plot(ema_20)

    positions = signal.crossover.loc[start_date:end_date]
    open_position_index = positions[positions == 1].index
    ax.scatter(
        x=open_position_index,
        y=signal.ema_10[open_position_index],
        marker="^",
        s=ARROW_SIZE,
        color="g"
    )

    close_position_index = positions[positions == -1].index
    ax.scatter(
        x=close_position_index,
        y=signal.ema_10[close_position_index],
        marker="v",
        s=ARROW_SIZE,
        color="r"
    )

    date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    x_axis_dates = open_position_index.union(close_position_index).union(date_range)
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["EMA_10", "EMA_20", "Buy", "Sell"])
    ax.grid()
    return fig
