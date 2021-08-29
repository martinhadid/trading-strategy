from configuration import STOCK, PERIOD
from plot.signals import plot_signals
from trading.trading_strategy import request_ticker, ticker_close_price, \
    price_moving_average_10_days, price_moving_average_20_days, \
    generate_signals_from_crossovers, set_position


def app():
    ticker = request_ticker(ticker_name=STOCK, period=PERIOD)
    df_stock = ticker_close_price(df_ticker=ticker)
    df_stock["SMA_10"] = price_moving_average_10_days(df_stock)
    df_stock["SMA_20"] = price_moving_average_20_days(df_stock)
    df_stock_signals = generate_signals_from_crossovers(df_signals=df_stock)
    df_stock_position = set_position(df_signals=df_stock_signals)
    plot_signals(df=df_stock_position)


if __name__ == "__main__":
    app()
