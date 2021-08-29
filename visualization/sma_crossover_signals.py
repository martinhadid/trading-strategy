import matplotlib.pyplot as plt
import pandas as pd


def plot_sma_signals(df: pd.DataFrame):
    plt.figure(figsize=(20, 10))
    df["Close"].plot(color="k", label="Close Price")
    df["SMA_10"].plot(color="r", label="10-day SMA")
    df["SMA_20"].plot(color="b", label="20-day SMA")
    df["SMA_100"].plot(color="g", label="100-day SMA")
    plt.plot(df[df["position"] == 1].index, df["SMA_10"][df["position"] == 1], marker="^",
             markersize=15, color="g", label="buy")
    plt.plot(df[df["position"] == -1].index, df["SMA_20"][df["position"] == -1],
             marker="v", markersize=15, color="r", label="sell")
    plt.ylabel("Price", fontsize=15)
    plt.xlabel("Date", fontsize=15)
    plt.title("Trading Strategy Signals", fontsize=20)
    plt.legend()
    plt.grid()
    plt.savefig(fname="SMA Crossover")
