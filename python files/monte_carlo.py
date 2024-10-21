import numpy as np
import pandas as pd
import api as api

# Get stock data for "stock"
api.ticker = "NVDA"  # Manual override
ticker_history = api.get_stock_history(api.ticker, "1mo")
ticker_close = ticker_history["Close"]

# Calculate necessary values
avg_return = np.mean(ticker_history["Close"].pct_change().dropna())
variance = np.var(ticker_history["Close"].pct_change().dropna())
drift = avg_return - (0.5 * variance)
ticker_std = np.std(ticker_history["Close"].pct_change().dropna())

# Periodic daily return
pdr_log = np.log(ticker_close.iloc[-1] / ticker_close.iloc[-2])
pdr_simple = (ticker_close.iloc[-1] - ticker_close.iloc[-2]) / ticker_close.iloc[-2]

# Ensure all arrays are of the same length
length = len(ticker_close)
avg_return_list = [avg_return] * length
variance_list = [variance] * length
drift_list = [drift] * length
pdr_log_list = [pdr_log] * length
pdr_simple_list = [pdr_simple] * length

# Create a DataFrame to store the results
df = pd.DataFrame({
    'Close Prices': ticker_close.tolist(),
    'Average Return': avg_return_list,
    'Variance': variance_list,
    'Drift': drift_list,
    'Price Daily Return (Log)': pdr_log_list,
    'Price Daily Return (Simple)': pdr_simple_list
})

# Write the DataFrame to a CSV file
df.to_csv('retrieved_data.csv', index=False)

print("Data has been retrieved and saved to 'retrieved_data.csv'")
