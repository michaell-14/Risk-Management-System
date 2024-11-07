import api 
import numpy as np
import pandas as pd
import beta_func as bf

api.ticker = "XEQT.TO"
ticker_history = api.get_stock_history(api.ticker, "1mo")
close = ticker_history["Close"]
ticker_return = api.get_stock_returns(api.ticker, "1mo")


def volatility(stock_tick, days):
    api.ticker = stock_tick
    variance = bf.var(stock_tick)
    print("Variance of ", stock_tick,": ", variance)
    v = (variance**0.5)*((days)**0.5)*100
    v = round(v, 4)
    
    print(f"Volatility of {stock_tick} over {days} days: {v}%")
    
    return v

volatility("NVDA", 252) #annual volatility
