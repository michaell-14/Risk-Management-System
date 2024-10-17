import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import test_api as api

#252 trading days in a year, 21 trading days in a month, 63 trading days in a quarter
# Beta = Covariance(Stock, Market) / Variance(Market)
# compare to "api.get_beta(api.ticker)""
#going to be using the S&P 500 as the market benchmark

api.ticker = "NVDA" #manual override
api.get_stock_history(api.ticker)
api.get_stock_returns(api.ticker)

api.ticker = "^GSPC" #manual override for S&P 500
api.get_stock_history(api.ticker)
api.get_stock_returns(api.ticker)


