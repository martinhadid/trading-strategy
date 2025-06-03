"""Plot for Relative Strength Index (RSI)."""

import datetime

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


def plot_rsi(
    strategy: pd.Series, start_date: datetime.date, end_date: datetime.date
) -> Figure:
    """Plots the Relative Strength Index (RSI) for a given strategy.

    Args:
        strategy (pd.Series): A Pandas Series containing the RSI values.
        start_date (datetime.date): The start date for plotting the RSI.
        end_date (datetime.date): The end date for plotting the RSI.

    Returns:
        Figure: A matplotlib Figure object displaying the RSI line and overbought/oversold levels.
    """
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    strategy = strategy.loc[start_date:end_date]
    ax.plot(strategy)
    ax.axhline(y=20, color="k", linestyle="-")
    ax.axhline(y=80, color="k", linestyle="-")
    ax.tick_params(axis="x", rotation=config.plots.x_rotation)
    ax.legend(["RSI", "Oversold", "Overbought", "Oversold", "Top", "Bottom"])
    return fig
