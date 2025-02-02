from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import pandas as pd

from trading_strategy.config import config_parser

config = config_parser.parse_from_file(config_file="config.toml")


def plot_fibonacci_retracements(
    strategy: pd.DataFrame, start_date: str, end_date: str
) -> Figure:
    fig, ax = plt.subplots(figsize=config.plots.fig_size)
    return fig
