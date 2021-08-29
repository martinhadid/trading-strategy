import pandas as pd
import yfinance as yf

from configuration import STOCK, PERIOD
from trading.sma_crossover_strategy import set_trading_strategy
from trading.tendency import stock_tendency
from visualization.sma_crossover_signals import plot_sma_signals


def request_ticker_prices(ticker_name: str, period: str) -> pd.DataFrame:
    ticker = yf.Ticker(ticker_name)
    return ticker.history(period=period).loc[:, ["Open", "Low", "High", "Close"]]


def app():
    df_ticker = request_ticker_prices(ticker_name=STOCK, period=PERIOD)
    df_stock = stock_tendency(df_stock=df_ticker)
    df_stock_position = set_trading_strategy(df_stock=df_stock)
    plot_sma_signals(df=df_stock_position)


if __name__ == "__main__":
    app()
