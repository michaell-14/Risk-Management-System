import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api


# Get stock data for "stock"
api.ticker = "NVDA"  # Manual override
ticker_price = api.get_current_stock_price(api.ticker) #will return the stock returns for the last month
ticker_history = api.get_stock_history(api.ticker, "1mo")

ticker_close = ticker_history["Close"]
ticker_close_list = ticker_close.tolist()
print("close: ", ticker_close_list) #this will return the closing prices for the last month in a list

ticker_average = np.mean(ticker_close_list)
print("average: ", ticker_average) #this will return the average closing price for the last month


#Simple Moving Average (SMA)
#SMA = (Sum of Price from N periods) / N

n = len(ticker_close_list) #number of trading days --> this would give N = the period called in function

sma_stock = sum(ticker_close_list)/n
print("Simple Moving Average: ", sma_stock)

#Exponential Moving Average (EMA)

