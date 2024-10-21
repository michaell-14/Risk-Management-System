import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import api as api
import beta_calc

# 252 trading days in a year, 21 trading days in a month, 63 trading days in a quarter

#pdr = ln(today_price/yesterday_price) #periodic daily return
#drift = avg(daily_return) - 0.5*var

#GBM = S(t) = S(t-1) * e^(drift + stdev * Z)
#Z = random number from standard normal distribution

api.ticker = "NVDA"  # Manual override
ticker_return = api.get_stock_returns(api.ticker) 
ticker_history = api.get_stock_history(api.ticker)
ticker_price = api.get_current_stock_price(api.ticker)
ticker_std = np.std(ticker_return)
avg_return = np.mean(ticker_return)
t = len(ticker_return)

variance = np.var(ticker_return)


drift = avg_return - (0.5 * variance)   


#periodic daily return
pdr_log = np.log(ticker_price / ticker_history["Close"].iloc[-2])


pdr_simple = (ticker_history["Close"].iloc[-1] - ticker_history["Close"].iloc[-2]) / ticker_history["Close"].iloc[-2]


#GBM
#GBM predicts the stock price at a future time
Z = np.random.standard_normal()
S = ticker_price * np.exp(drift + ticker_std * Z)

print(f"Average Return for {api.ticker}: {avg_return:.4f}")
print(f"Variance: {variance:.4f}")
print(f"Drift: {drift:.4f}")
print(f"Price Daily Return (Log): {pdr_log:.4f}")
print(f"Price Daily Return (Simple): {pdr_simple:.4f}")
print(f"Geometric Brownian Motion (Predicted Price): {S:.4f}")

for i in range(100):
    Z = np.random.standard_normal()
    S = ticker_price * np.exp(drift + ticker_std * Z)
    print(f"Predicted Price {i+1}: {S:.4f}")

