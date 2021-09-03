import matplotlib.pyplot as plt
import pandas as pd

FIG_SIZE = (20, 10)


def plot_sma_signals(df: pd.DataFrame):
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(df.index, df["Close"])
    ax.plot(df.index, df["SMA_10"])
    ax.plot(df.index, df["SMA_20"])
    # ax.plot(df.index, df["SMA_100"], color="g")
    plt.scatter(
        df[df["position"] == 1]["SMA_10"].index,
        df["SMA_10"][df["position"] == 1],
        marker="^", s=150, color="g"
    )
    plt.scatter(
        df[df["position"] == -1]["SMA_10"].index,
        df["SMA_10"][df["position"] == -1],
        marker="v", s=150, color="r"
    )
    ax.legend(["Close Price", "SMA_10", "SMA_20", "Buy", "Sell"])
    ax.set(xlabel="Date", ylabel="Close Price")
    ax.grid()
    fig.savefig(fname="visualization/output/SMA Crossover")
    return fig
