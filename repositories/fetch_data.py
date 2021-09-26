import yfinance as yf

from repositories.data.stock import Stock

PERIOD = "1y"
INTERVAL = "1d"


def request_ticker(ticker_name: str) -> (Stock, Stock, Stock):
    stock_data = yf.download(tickers=ticker_name, period=PERIOD, interval=INTERVAL)
    stock_close = Stock(price=stock_data.loc[:, "Close"])
    stock_high = Stock(price=stock_data.loc[:, "High"])
    stock_low = Stock(price=stock_data.loc[:, "Low"])
    return stock_close, stock_high, stock_low
