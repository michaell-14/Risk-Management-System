import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api

# 252 trading days in a year, 21 trading days in a month, 63 trading days in a quarter
# Beta = Covariance(Stock, Market) / Variance(Market)
# Compare to "api.get_beta(api.ticker)"
# Using the S&P 500 as the market benchmark

# Get stock data for "stock"
api.ticker = "NVDA"  # Manual override
ticker_history = api.get_stock_history(api.ticker)
ticker_return = api.get_stock_returns(api.ticker)
avg_return = np.mean(ticker_return)
print("Average Return: ", api.ticker, avg_return)

# Get stock data for S&P 500, ^GSPC
api.ticker = "^GSPC"  # Manual override for S&P 500
ticker_1_history = api.get_stock_history(api.ticker)
ticker_1_return = api.get_stock_returns(api.ticker)  # Dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment
avg_return1 = np.mean(ticker_1_return)
print("Average Return: ", api.ticker, avg_return1)

print("-------------------------------------------------------------------------------------------------")

#calculates the average return of the stock divided by the average return of the S&P 500
#i.e the ratio of the stock's return to the S&P 500's return
return_ratio = avg_return / avg_return1
print("Return Ratio:", return_ratio)

#Variability of the STOCKS's returns
vair = np.var(ticker_return)
vair_calc = ((ticker_return - avg_return)**2).sum()/(len(ticker_return)-1)
vair_avg = (vair + vair_calc)/2
print("Variance: ", vair)
print("Variance Calculation: ", vair_calc)
print("Average Variance: ", vair_avg)

#Variability of the S&P 500's returns; used for Beta calculation
var_bm = np.var(ticker_1_return)

#Covariance of the stock's returns with the S&P 500's returns
cov_calc = ((ticker_return - avg_return)*(ticker_1_return - avg_return1)).sum()/(len(ticker_return)-1)
print("Covariance Calculation: ", cov_calc)

#Beta Calculation
#Beta = Covariance(Stock, or Market) / Variance(Market (benchmark))
beta_calc = cov_calc/var_bm
print("Beta: ", beta_calc)
#Beta < 0 means the stock moves in the opposite direction of the market, Beta = 0 means the stock is uncorrelated with the market, Beta > 0 means the stock moves in the same direction as the market
#beta of ^GSPC = 1.0 --> market benchmark




# Plot returns comparison
plt.figure(figsize=(14, 7))
plt.plot(ticker_return.index, ticker_return, label='NVDA Returns')
plt.plot(ticker_1_return.index, ticker_1_return, label='S&P 500 Returns')
plt.title('NVDA vs S&P 500 Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
#plt.show()
