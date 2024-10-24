import matplotlib.pyplot as plt
import numpy as np
import monte_carlo as mc
from numpy.random import normal

print(mc.api.ticker)
csv_file = r'C:\Users\micha\OneDrive\Documents\GitHub\Stocks-Project\python_files\simulation_results.csv'
df = mc.pd.read_csv(csv_file)
print(df)

std_dev_price = np.std(df['Predicted Price'])
avg_price = np.mean(df['Predicted Price']) 

mu = 50
sigma = 10

size = [10,50,100,1000,10000]

for i in range(len(size)):
    #sample = np.(mu, sigma, size[i])
    sample = normal(avg_price, std_dev_price, size[i])
    plt.subplot(2, 2, i+1)
    plt.hist(sample, bins=20)
    plt.title('%d samples' % size[i])
    plt.xticks([])
plt.show()

#std_dev of the predicted price
plt.figure(figsize=(14, 7))
plt.plot(df['Simulation'], df['Predicted Price'], label='Predicted Price', color='blue')
plt.fill_between(df['Simulation'], df['Predicted Price'] - std_dev_price, df['Predicted Price'] + std_dev_price, color='b', alpha=0.1)
plt.xlabel('Simulation')
plt.ylabel('Predicted Price')
plt.title('Predicted Prices Over Simulations')
plt.legend()
#plt.show()
