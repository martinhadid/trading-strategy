import datetime

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


def plot_rsi(
    strategy: pd.Series, start_date: datetime.date, end_date: datetime.date
) -> Figure:
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    strategy = strategy.loc[start_date:end_date]
    ax.plot(strategy)
    ax.axhline(y=20, color="k", linestyle="-")
    ax.axhline(y=80, color="k", linestyle="-")
    ax.tick_params(axis="x", rotation=config.plots.x_rotation)
    ax.legend(["RSI", "Oversold", "Overbought", "Oversold", "Top", "Bottom"])
    return fig
