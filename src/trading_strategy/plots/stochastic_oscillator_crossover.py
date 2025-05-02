import datetime

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


def plot_stochastic_oscillator(
    strategy: pd.DataFrame,
    start_date: datetime.date,
    end_date: datetime.date,
) -> Figure:
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    strategy = strategy.loc[start_date:end_date]

    k = strategy["k"]
    d = strategy["d"]

    ax.plot(k)
    ax.plot(d, linestyle="--")
    ax.axhline(y=30, color="k", linestyle="-")
    ax.axhline(y=70, color="k", linestyle="-")

    positions = strategy["crossover"]
    open_position_index = positions[positions == 1].index
    ax.scatter(
        x=open_position_index,
        y=k[open_position_index],
        marker="^",
        s=config.plots.arrow_size,
        color="g",
    )

    close_position_index = positions[positions == -1].index
    ax.scatter(
        x=close_position_index,
        y=k[close_position_index],
        marker="v",
        s=config.plots.arrow_size,
        color="r",
    )
    date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    x_axis_dates = open_position_index.union(close_position_index).union(date_range)
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=config.plots.x_rotation)
    ax.legend(["%K", "%D", "Oversold", "Overbought", "Buy", "Sell"])
    return fig
