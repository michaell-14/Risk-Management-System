import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import api as api


# Get stock data for "stock"
api.ticker = "^GSPC"  
ticker_price = api.get_current_stock_price(api.ticker) #will return the stock returns for the last month
ticker_history = api.get_stock_history(api.ticker, "1mo")

ticker_close = ticker_history["Close"]
ticker_close_list = ticker_close.tolist()
#this will return the closing prices for the last month in a list

ticker_average = np.mean(ticker_close_list)
 #this will return the average closing price for the last month

#standard deviation
ticker_std = np.std(ticker_close_list)

#volatility
ticker_volatility = ticker_std / np.mean(ticker_close_list)
print("Volatility: ", ticker_volatility)



print("Close Prices: ", ticker_close_list)  # This will return the stock closing prices for the last month
print("Average Closing Price: ", ticker_average)  # This will return the average closing price for the last month
print("Standard Deviation: ", ticker_std)  # This will return the standard deviation of the closing prices



# Simple Moving Average (SMA)
# SMA = (Sum of Price from N periods) / N
sma_stock = ticker_close.rolling(window=20).mean()
print("Simple Moving Average: ", sma_stock.iloc[-1])

#we dont use sma_stock because ema_stock is the exponential moving average and is more responsive to price changes

# Exponential Moving Average (EMA)
# EMA = (Price_today * k) + (EMA_yesterday * (1 - k))
# where k = 2 / (N + 1)
s = 2 / (len(ticker_close_list) + 1)
ema_stock = [ticker_close_list[0]]  # Initialize EMA with the first closing price

for i in range(1, len(ticker_close_list)):
    ema_stock.append((ticker_close_list[i] - ema_stock[-1]) * s + ema_stock[-1])

# Convert EMA list to a pandas Series
ema_stock_series = pd.Series(ema_stock, index=ticker_close.index)
ema_stock = pd.Series(ema_stock, index=ticker_close.index) #converting the list to a pandas series; reversing what I did in the beginning
print("Exponential Moving Average: ", ema_stock)

# Plotting the data
plt.figure(figsize=(14, 7))
plt.plot(ticker_close.index, ticker_close, label=f'{api.ticker} Close Prices')
plt.plot(ticker_close.index, ema_stock, label=f'{api.ticker} EMA')
plt.title(f'{api.ticker} Historical Prices with SMA and EMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
#plt.show()
