import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import api as api

def var(stock_ticker):
    api.ticker = stock_ticker 
    ticker_history = api.get_stock_history(api.ticker, "1mo")
    ticker_return = api.get_stock_returns(api.ticker, "1mo")  # Dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment
    avg_return = np.mean(ticker_return)

    #Variability of the STOCKS's returns
    var_calc = ((ticker_return - avg_return)**2).sum()/(len(ticker_return)-1)
    return var_calc

def calc_beta(stock_tick, bm_tick, period):
   # Get stock data for "stock"
    api.ticker = stock_tick 
    ticker_history = api.get_stock_history(api.ticker, period)
    ticker_return = api.get_stock_returns(api.ticker, period)  # Dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment
    avg_return = np.mean(ticker_return)
    print("Average Return: ", api.ticker, avg_return)


    api.ticker = bm_tick  
    ticker_1_return = api.get_stock_returns(api.ticker, "1mo")  # Dates are forms of YYYY-MM-DD; the first date listed is the oldest date in the data segment
    avg_return1 = np.mean(ticker_1_return)
    print("Average Return: ", api.ticker, avg_return1)

    print("-------------------------------------------------------------------------------------------------")

    #the ratio of the stock's return to the S&P 500's return
    return_ratio = avg_return / avg_return1
    print("Return Ratio:", return_ratio)

    a = var(stock_tick)
    print("Variane of ", stock_tick,": ", a)
    b = var(bm_tick)
    print("Variane of ", bm_tick,": ", b)

    var_bm = ((ticker_1_return - avg_return1)**2).sum()/(len(ticker_1_return)-1)

    #Covariance of the stock's returns with the S&P 500's returns
    cov_calc = ((ticker_return - avg_return)*(ticker_1_return - avg_return1)).sum()/(len(ticker_return)-1)
    print("Covariance Calculation: ", cov_calc)

    #Beta Calculation
    #Beta = Covariance(Stock, or Market) / Variance(Market (benchmark))
    beta_calc = cov_calc/var_bm
    print("Beta: ", beta_calc)

    #Beta < 0 means the stock moves in the opposite direction of the market, Beta = 0 means the stock is uncorrelated with the market, Beta > 0 means the stock moves in the same direction as the market
    #Beta  < or > 1 means the stock is more volatile than the market, by that factor
    #beta of ^GSPC = 1.0 --> market benchmark

    return beta_calc


calc_beta("NVDA", "^GSPC", "1mo")
