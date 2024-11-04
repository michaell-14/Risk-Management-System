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
max_bin_index = np.argmax(hist) #argmax() returns the indices of the maximum values along an axis; in this case, the index of the bin with the highest frequency
max_freq = np.max(hist) #max() returns the maximum value of the array; in this case, the highest frequency
print(max_freq)
max_bins = np.where(hist == max_freq) #where() returns the indices of an array where condition is satisfied

#print(max_bins) --> this is a tuple, we need to index it to get the actual value

max_bin_indices = max_bins[0] #need to do this to get the indices of the bins with the highest frequency, otherwise it returns a tuple and we dont want that
midpoints = (bin_edges[max_bin_indices] + bin_edges[max_bin_indices + 1]) / 2
print(midpoints)

most_probable_price = np.mean(midpoints)
#most_probable_price1 = midpoints[0] #this has nothing to do with the most probable price, this is just the midpoint of the first bin with the highest frequency, therefore doesnt mean much to me

print(f"Most probable price: {most_probable_price}") #this gives an estimate of the most probable price, with cents of the closing based on testing

#print(f"Most probable price1: {most_probable_price1}") #this is inaccurate, dont use this

#raw plotting yipeee
plt.figure(figsize=(14, 7))
plt.plot(bin_edges[1:], hist)  # Plot histogram
plt.axhline(y=hist[max_bin_index], color='g', linestyle='--', label='Max Frequency')  # Add horizontal line for most probable price
plt.axvline(x=most_probable_price, color='r', linestyle='--', label='Most Probable Price')  # Add vertical line for most probable price
plt.xlabel('Predicted Price')
plt.ylabel('Frequency')
plt.legend()
plt.title('Raw Histogram of Predicted Prices')
plt.show()
#above line is like: (x1 + x2) / 2, where x1 and x2 are the edges of the bin with the highest frequency, this is just the bin that is the highest on the plot
#except using the bin edges from histogram; max_bin_index is the index of the bin with the highest frequency, +1 is the next bin



plt.figure(figsize=(14, 7))
plt.hist(df['Predicted Price'], bins=250, density=True, alpha=0.6, color='blue', label='Empirical Distribution')  # Creates histogram with bars
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
