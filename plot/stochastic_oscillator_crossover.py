import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from plot.settings import FIG_SIZE, X_ROTATION, ARROW_SIZE


def plot_stochastic_oscillator(strategy: pd.DataFrame, start_date: str,
                               end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    strategy = strategy.loc[start_date: end_date]

    k = strategy.loc[:, "k"]
    d = strategy.loc[:, "d"]

    ax.plot(k)
    ax.plot(d, linestyle="--")
    ax.axhline(y=30, color="r", linestyle="-")

    open_position_index = strategy.loc[strategy["crossover"] == 1].index
    ax.scatter(
        x=open_position_index,
        y=k[open_position_index],
        marker="^",
        s=ARROW_SIZE,
        color="g"
    )

    close_position_index = strategy.loc[strategy["crossover"] == -1].index
    ax.scatter(
        x=close_position_index,
        y=k[close_position_index],
        marker="v",
        s=ARROW_SIZE,
        color="r"
    )
    date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    x_axis_dates = open_position_index.union(close_position_index).union(date_range)
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["%K", "%D", "Oversold", "Buy", "Sell"])
    return fig

    # volume
    # ax2 = ax.twinx()
    # ax2.bar(x=df.index, height=df["Volume"])
