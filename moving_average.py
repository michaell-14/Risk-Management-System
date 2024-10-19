import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api


# Get stock data for "stock"
api.ticker = "NVDA"  # Manual override
ticker_return = api.get_stock_returns(api.ticker, period='1mo') #will return the stock returns for the last month
avg_return = np.mean(ticker_return)
print("Average Return: ", api.ticker, avg_return)

# Get stock data for S&P 500, ^GSPC
api.ticker = "^GSPC"  # Manual override for S&P 500
ticker_1_return = api.get_stock_returns(api.ticker, period='1mo')  
avg_return1 = np.mean(ticker_1_return)
print("Average Return: ", api.ticker, avg_return1)

#Simple Moving Average (SMA)
#SMA = (Sum of Price from N periods) / N

len(ticker_return) #number of trading days --> this would give 1 ytd N = 252; the sma for the last year correlated trading days 

sma_stock = (ticker_return.sum())/len(ticker_return) 
print("Simple Moving Average: ", sma_stock)

#Exponential Moving Average (EMA)

