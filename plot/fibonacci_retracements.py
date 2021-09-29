import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from plot.settings import FIG_SIZE


def plot_fibonacci_retracements(strategy: pd.DataFrame, start_date: str,
                                end_date: str) -> Figure:
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    return fig
