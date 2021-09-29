import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from plot.settings import FIG_SIZE, X_ROTATION


def plot_rsi(strategy: pd.Series, start_date: str, end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    strategy = strategy.loc[start_date: end_date]

    ax.plot(strategy)
    ax.axhline(y=20, color="k", linestyle="-")
    ax.axhline(y=80, color="k", linestyle="-")

    # top_and_bottom = strategy["crossover"]
    # top_position_index = top_and_bottom[top_and_bottom == 1].index
    # ax.scatter(
    #     x=top_position_index,
    #     y=rsi[top_position_index],
    #     marker="^",
    #     s=ARROW_SIZE,
    #     color="g"
    # )
    #
    # bottom_position_index = top_position_index[top_position_index == -1].index
    # ax.scatter(
    #     x=bottom_position_index,
    #     y=rsi[bottom_position_index],
    #     marker="v",
    #     s=ARROW_SIZE,
    #     color="r"
    # )
    # date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    # x_axis_dates = top_position_index.union(bottom_position_index).union(date_range)
    # ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["RSI", "Oversold", "Overbought", "Oversold", "Top", "Bottom"])
    return fig
