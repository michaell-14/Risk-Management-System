import api 
import numpy as np
import pandas as pd
import beta_func as bf
import matplotlib.pyplot as plt

def volatility(stock_tick, days):
    api.ticker = stock_tick
    variance = bf.var(stock_tick)
    print("Variance of ", stock_tick,": ", variance)
    v = (variance**0.5)*((days)**0.5)*100
    v = round(v, 4)
    
    print(f"Volatility of {stock_tick} over {days} days: {v}%")
    
    return v

volatility("NVDA", 252) #annual volatility

#plot volatility
def plot_vola_percentage(stock_ticker, period):
    api.ticker = stock_ticker
    ticker_return = api.get_stock_returns(api.ticker, period)
    vola_list = []
    #for annual volatility, we use 252 trading days in a year
    for i in range(1, len(ticker_return)):
        vola = np.std(ticker_return[:i])*np.sqrt(252)*100  #needed to do different method because of the way the returns are gotten, and the way the volatility is calculated
        #^takes std of the returns :i (up to the current day), multiplies by sqrt of the number of trading days in a year, and multiplies by 100 to get percentage
        vola_list.append(vola)

    print(np.std(ticker_return))
    print(vola_list[-1])

    plt.figure(figsize=(14,7))
    plt.plot(vola_list)
    plt.title(f"{stock_ticker} Volatility")
    plt.xlabel("Days")
    plt.ylabel("Volatility (%)")
    plt.show()

plot_vola_percentage("NVDA", "1y")
