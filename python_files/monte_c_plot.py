import matplotlib.pyplot as plt
import numpy as np
import monte_carlo as mc
from numpy.random import normal
from scipy.stats import norm

plt.close('all')

print(mc.api.ticker)
csv_file = r'C:\Users\micha\OneDrive\Documents\GitHub\Stocks-Project\python_files\simulation_results.csv'
df = mc.pd.read_csv(csv_file)
print(df)

std_dev_price = np.std(df['Predicted Price'])
avg_price = np.mean(df['Predicted Price']) 

predicted_price = df['Predicted Price']


#Standard Div
rolling_std = df['Predicted Price'].rolling(window=20).std() #rolling standard deviation; syntax is df['column'].rolling(window=20).std()
#window is the number of observations used for calculating the statistic; std() calculates the standard deviation

'''# Plot standard deviation of the predicted price vs the number of simulations
plt.figure(figsize=(14, 7))
plt.plot(df['Simulation'], rolling_std, label='Rolling Std Dev of Predicted Price', color='orange')
plt.xlabel('Simulation')
plt.ylabel('Price of label')
plt.title('Std over time')
plt.legend()
plt.show()'''

# Method 2: Empirical Probability from histogram (frequency count within range)

price_range = [100, 150]  # Example range (adjust based on your price range of interest)
predicted_price = df['Predicted Price']
count_in_range = ((predicted_price >= price_range[0]) & (predicted_price <= price_range[1])).sum()
probability_empirical = count_in_range / len(predicted_price)
print(f"Empirical Probability of price between {price_range[0]} and {price_range[1]}: {probability_empirical:.4f}")
'''
plt.figure(figsize=(14,7))
plt.plot(df['Simulation'], predicted_price, label='Predicted Price', color='orange')
plt.xlabel('Simulation')
plt.ylabel('Price')
plt.title('Predicted Price over Simulations')
plt.legend()
#plt.show()'''
#bins is the number of bars in the histogram
# Plot histogram with bars for predicted prices

print("Predicted Price == ", predicted_price)
plt.figure(figsize=(14, 7))
plt.hist(df['Predicted Price'], bins=200, density=True, alpha=0.6, color='blue', label='Empirical Distribution')  # Creates histogram with bars
# Overlay normal distribution as a line
xmin, xmax = plt.xlim()  # Set the x-axis limits to match histogram
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, avg_price, std_dev_price)
plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution (PDF)')  # Overlay PDF as a lined
plt.xlabel('Predicted Price')
plt.ylabel('Density')
plt.title('Histogram of Predicted Prices with Normal PDF Overlay')
plt.legend()
plt.show()  
