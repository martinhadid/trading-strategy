"""Plot for stock price with exponential moving average."""

import datetime

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

from trading_strategy.config import config_parser
from trading_strategy.utils import exponential_moving_average

config = config_parser.parse_from_file(config_file="config.toml")


def plot_price(
    stock: pd.DataFrame, start_date: datetime.date, end_date: datetime.date
) -> Figure:
    """Plots the stock's closing price along with 100-day and 200-day Exponential Moving Averages (EMAs).

    Args:
        stock (pd.DataFrame): A DataFrame containing stock data, expected to have a 'Close' column.
        start_date (datetime.date): The start date for plotting the data.
        end_date (datetime.date): The end date for plotting the data.

    Returns:
        Figure: A matplotlib Figure object displaying the closing price and the two EMA lines.
    """
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    close_price = stock["Close"]
    ema_100 = exponential_moving_average(price=close_price, days=100, name="price")
    ema_200 = exponential_moving_average(price=close_price, days=200, name="price")
    price = close_price.loc[start_date:end_date]
    ema_100 = ema_100.loc[start_date:end_date]
    ema_200 = ema_200.loc[start_date:end_date]
    ax.plot(price)
    ax.plot(ema_100)
    ax.plot(ema_200)
    ax.tick_params(axis="x", rotation=config.plots.x_rotation)
    ax.legend(["Close Price", "EMA_100", "EMA_200"])
    ax.grid()
    return fig
