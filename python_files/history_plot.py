import api as api
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import scipy.stats as stats
import time
import matplotlib.animation as animation

api.ticker = "NVDA"
api.period = "1mo" #for historical data
ticker_history = api.get_stock_history(api.ticker, api.period)
ticker_price = ticker_history["Close"]
current_price = api.get_current_stock_price(api.ticker)

def plot_ticker_historical():
    plt.figure(figsize=(14, 7))
    plt.plot(ticker_price.index, ticker_price, label='NVDA Price', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Stock Price over Time')
    plt.show()


def plot_ticker_current(frame):
    ticker_history = api.get_stock_history(api.ticker, api.period)
    ticker_price = ticker_history["Close"]
    current_price = api.get_current_stock_price(api.ticker)

    plt.clf()
    plt.plot(ticker_price.index, ticker_price, label='Stock Price', color='orange')
    plt.axhline(y=current_price, color='r', linestyle='-', label='Current Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Stock Price over Time with Current Price')

def update_graph(interval = 1000): #interval is in milliseconds
    fig = plt.figure(figsize=(14, 7))
    ani = animation.FuncAnimation(fig, plot_ticker_current, interval=interval)
    plt.show()

# Continuously update the graph
update_graph(10000) 
