import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from utils.plots import FIG_SIZE


def plot_stochastic_oscillator_signals(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    ax.plot(df["%K"])
    ax.plot(df["%D"])
    ax.axhline(y=70, color="r", linestyle="-")
    ax.axhline(y=30, color="r", linestyle="-")
    # volume
    # ax2 = ax.twinx()
    # ax2.bar(x=df.index, height=df["Volume"])
    ax.legend(["%K", "%D", "Overbought", "Oversold"])
    return fig
