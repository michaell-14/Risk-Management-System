import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api

# 252 trading days in a year, 21 trading days in a month, 63 trading days in a quarter
# Beta = Covariance(Stock, Market) / Variance(Market)
# Compare to "api.get_beta(api.ticker)"
# Using the S&P 500 as the market benchmark

# Get stock data for NVDA
api.ticker = "NVDA"  # Manual override
ticker_history = api.get_stock_history(api.ticker)
ticker_return = api.get_stock_returns(api.ticker)
avg_return = np.mean(ticker_return)
print("Average Return: ", api.ticker, avg_return)



print("-------------------------------------------------------------------------------------------------")

# Get stock data for S&P 500, ^GSPC
api.ticker = "AMD"  # Manual override for S&P 500
ticker_1_history = api.get_stock_history(api.ticker)
ticker_1_return = api.get_stock_returns(api.ticker)  # Dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment
avg_return1 = np.mean(ticker_1_return)
print("Average Return: ", api.ticker, avg_return1)

#calculates the average return of the stock divided by the average return of the S&P 500
calc = avg_return / avg_return1
print(calc)

# Plot returns comparison
plt.figure(figsize=(14, 7))
plt.plot(ticker_return.index, ticker_return, label='NVDA Returns')
plt.plot(ticker_1_return.index, ticker_1_return, label='AMD Returns')
plt.title('NVDA vs AMD Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.show()
