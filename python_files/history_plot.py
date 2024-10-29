import api as api
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import scipy.stats as stats

api.ticker = "NVDA"
api.period = "1y"
ticker_history = api.get_stock_history(api.ticker, api.period)
ticker_price = ticker_history["Close"]


plt.figure(figsize=(14, 7))
plt.plot(ticker_price.index, ticker_price, label='NVDA Price')
plt.title('NVDA Price over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
