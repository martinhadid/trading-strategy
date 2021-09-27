import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from utils import exponential_moving_average
from visualization.settings import X_ROTATION, FIG_SIZE


def plot_price(stock: pd.DataFrame, start_date: str, end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    close_price = stock.loc[:, "Close"]
    price = close_price.loc[start_date:end_date]
    ema_100 = exponential_moving_average(price=price, days=100, name="price")
    ax.plot(price)
    ax.plot(ema_100)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["Close Price", "EMA_100"])
    ax.grid()
    return fig
