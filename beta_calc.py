import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api

#252 trading days in a year, 21 trading days in a month, 63 trading days in a quarter
# Beta = Covariance(Stock, Market) / Variance(Market)
# compare to "api.get_beta(api.ticker)""
#going to be using the S&P 500 as the market benchmark

api.ticker = "NVDA" #manual override
ticker_history = api.get_stock_history(api.ticker)
ticker_return = api.get_stock_returns(api.ticker)
avg_return = np.mean(ticker_return)

print("-------------------------------------------------------------------------------------------------")

api.ticker = "^GSPC" #manual override for S&P 500
ticker_1_history = api.get_stock_history(api.ticker) 
ticker_1_return = api.get_stock_returns(api.ticker) #dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment 

avg_return1 = np.mean(ticker_1_return)

calc = np.cov(ticker_return, ticker_1_return)
print("Covariance of Stock and Market: ", calc[0][1])
