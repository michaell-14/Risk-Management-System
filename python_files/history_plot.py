import api as api
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib.animation as animation

api.ticker = "SOXL"
api.period = "1mo" #for historical data
ticker_history = api.get_stock_history(api.ticker, api.period)
ticker_price = ticker_history["Close"]
current_price = api.get_current_stock_price(api.ticker)

'''
def plot_ticker_historical():
    plt.figure(figsize=(14, 7))
    plt.plot(ticker_price.index, ticker_price, label='NVDA Price', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Stock Price over Time')
   # plt.show()
'''
'''
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
'''

current_prices = []
def plot_live_pricing(frame):
    current_price = api.get_current_stock_price(api.ticker)
    current_prices.append(current_price)

    plt.clf()
    plt.plot(ticker_price.index, ticker_price, label='Stock Price', color='orange')
    plt.axhline(y=current_price, color='g', linestyle='-', label='Current Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Stock Price Live (10 second intervals)')

def update_graph(graph, interval = 1000): #interval is in milliseconds
    fig = plt.figure(figsize=(14, 7))
    ani = animation.FuncAnimation(fig, graph, interval=interval)
    plt.show()

update_graph(plot_live_pricing, 11000) #update every 10 seconds
