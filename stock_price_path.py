import numpy as np
import matplotlib.pyplot as plt
from calculate_payoff import simulate_stock_price
from calculate_payoff import S0, T, r, sigma, n, m

# Calculate the option payoff
def calculate_payoff(stock_paths, K, option_type="call"):
    if option_type == "call":
        payoffs = np.maximum(stock_paths[:, -1] - K, 0)  # Call option payoff
    else:
        payoffs = np.maximum(K - stock_paths[:, -1], 0)  # Put option payoff
    return payoffs

stock_paths = simulate_stock_price(S0, T, r, sigma, n, m)