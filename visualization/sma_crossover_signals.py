import matplotlib.pyplot as plt
import pandas as pd

FIG_SIZE = (20, 10)


def plot_sma_signals(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(df.index, df["Close"])
    ax.plot(df.index, df["SMA_10"])
    ax.plot(df.index, df["SMA_20"])

    open_position = df[df["position"] == 1]["SMA_10"]
    ax.scatter(
        open_position.index,
        open_position,
        marker="^",
        s=150,
        color="g"
    )
    for index, value in open_position.iteritems():
        ax.annotate(round(value), (index, value))

    close_position = df[df["position"] == -1]["SMA_10"]
    ax.scatter(
        close_position.index,
        close_position,
        marker="v",
        s=150,
        color="r"
    )

    for index, value in close_position.iteritems():
        ax.annotate(round(value), (index, value))

    ax.set_xticks(close_position.index.union(open_position.index))
    ax.tick_params(axis="x", rotation=90)
    ax.legend(["Close Price", "SMA_10", "SMA_20", "Buy", "Sell"])
    ax.set(xlabel="Date", ylabel="Close Price")
    ax.grid()
    return fig
