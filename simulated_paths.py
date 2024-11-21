import matplotlib.pyplot as plt
import numpy as np
from stock_price_path import stock_paths, calculate_payoff, T,n,r
from calculate_payoff import K

# Visualize some simulated paths
plt.figure(figsize=(10, 6))
plt.plot(np.linspace(0, T, n + 1), stock_paths.T[:, :10], lw=1)  # Plot first 10 simulated paths
plt.title('Simulated Stock Price Paths')
plt.xlabel('Time (Years)')  
plt.ylabel('Stock Price (USD)')  

# Calculate option payoff
option_type = "call"  # Choose between "call" or "put"
payoffs = calculate_payoff(stock_paths, K, option_type)

# Discount payoffs to present value and calculate the option price
option_price = np.exp(-r * T) * np.mean(payoffs)

# Annotate the chart with the option price
textstr = f"Estimated European {option_type.capitalize()} Option Price: {option_price:.2f} USD"
plt.text(0.05, 0.95, textstr, transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5, edgecolor='black'))

plt.savefig('Simulated_Paths.pdf', format = 'pdf')
plt.show()
#plt.close()
# 
