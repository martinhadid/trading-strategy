import pandas as pd
import yfinance as yf

from configuration import STOCK, PERIOD
from plot.signals import plot_signals
from trading.trading_strategy import set_trading_strategy


def request_ticker(ticker_name: str, period: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_name)
    return ticker.history(period=period)


def app():
    ticker = request_ticker(ticker_name=STOCK, period=PERIOD)
    df_stock_position = set_trading_strategy(ticker=ticker)
    plot_signals(df=df_stock_position)


if __name__ == "__main__":
    app()
