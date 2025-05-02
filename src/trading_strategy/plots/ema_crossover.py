import datetime

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


def plot_ema(
    strategy: pd.DataFrame, start_date: datetime.date, end_date: datetime.date
) -> Figure:
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    strategy = strategy.loc[start_date:end_date]

    ema_10 = strategy["ema_10"]
    ema_20 = strategy["ema_20"]

    ax.plot(ema_10)
    ax.plot(ema_20)

    positions = strategy["crossover"]
    open_position_index = positions[positions == 1].index
    ax.scatter(
        x=open_position_index,
        y=ema_10[open_position_index],
        marker="^",
        s=config.plots.arrow_size,
        color="g",
    )
    close_position_index = positions[positions == -1].index
    ax.scatter(
        x=close_position_index,
        y=ema_10[close_position_index],
        marker="v",
        s=config.plots.arrow_size,
        color="r",
    )

    date_range = pd.date_range(start=start_date, end=end_date, freq="MS")
    x_axis_dates = open_position_index.union(close_position_index).union(date_range)
    ax.set_xticks(x_axis_dates)
    ax.tick_params(axis="x", rotation=config.plots.x_rotation)
    ax.legend(["EMA_10", "EMA_20", "Buy", "Sell"])
    ax.grid()
    return fig
