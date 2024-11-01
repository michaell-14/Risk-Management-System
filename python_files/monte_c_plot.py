import matplotlib.pyplot as plt
import numpy as np
import monte_carlo as mc #this is the main monte carlo file, all the functions are in there and declarations
from numpy.random import normal
from scipy.stats import norm

plt.close('all')

print(mc.api.ticker)
csv_file = r'C:\Users\micha\OneDrive\Documents\GitHub\Stocks-Project\python_files\simulation_results.csv'
df = mc.pd.read_csv(csv_file)
print(df)

std_dev_price = np.std(df['Predicted Price'])
avg_price = np.mean(df['Predicted Price']) 



#Standard Div
rolling_std = df['Predicted Price'].rolling(window=20).std() #rolling standard deviation; syntax is df['column'].rolling(window=20).std()
#window is the number of observations used for calculating the statistic; std() calculates the standard deviation

# Method 2: Empirical Probability from histogram (frequency count within range) i think it works

price_range = [100, 150]  # Example range (adjust based on your price range of interest)
predicted_price = df['Predicted Price']
count_in_range = ((predicted_price >= price_range[0]) & (predicted_price <= price_range[1])).sum()
total_count = len(predicted_price) #this should equal the number of sims requested

#histogram of the predicted prices, based from monte_carlo sims
#bins is the number of bars in the histogram
hist, bin_edges = np.histogram(df['Predicted Price'], bins=5000)

# Find the bin with the highest frequency --> most probable value
max_bin_index = np.argmax(hist) 
most_prob_val = (bin_edges[max_bin_index] + bin_edges[max_bin_index + 1]) / 2
#above line is like: (x1 + x2) / 2, where x1 and x2 are the edges of the bin with the highest frequency, this is just the bin that is the highest on the plot
#except using the bin edges from histogram; max_bin_index is the index of the bin with the highest frequency, +1 is the next bin

print(f"Most Probable Predicted Price: {most_prob_val}")


#Plot histogram with bars for predicted prices

plt.figure(figsize=(14, 7))
plt.hist(df['Predicted Price'], bins=100, density=True, alpha=0.6, color='blue', label='Empirical Distribution')  # Creates histogram with bars
# Overlay normal distribution
xmin, xmax = plt.xlim()  # Set the x-axis limits to match histogram
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, avg_price, std_dev_price)
plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution (PDF)')  # Overlay PDF as a lined
plt.xlabel('Predicted Price')
plt.ylabel('Density')
plt.title('Histogram of Predicted Prices with Normal PDF Overlay')
plt.legend()
plt.show()  
