from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from repositories.data.stock import Stock
from visualization.settings import X_ROTATION, FIG_SIZE


def plot_price(stock: Stock, start_date: str, end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    price = stock.price.loc[start_date:end_date]
    ema_100 = stock.exponential_moving_average(days=100, name="price")
    ema_100 = ema_100.loc[start_date:end_date]
    ax.plot(price)
    ax.plot(ema_100)
    ax.tick_params(axis="x", rotation=X_ROTATION)
    ax.legend(["Close Price", "EMA_100"])
    ax.grid()
    return fig
