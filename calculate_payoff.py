import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100  # Initial stock price
K = 110   # Strike price
T = 1.0   # Time to maturity (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility
n = 1000  # Number of time steps
m = 10000  # Number of simulations

# Simulate stock price paths
def simulate_stock_price(S0, T, r, sigma, n, m):
    dt = T / n  # Time step
    stock_paths = np.zeros((m, n + 1))
    stock_paths[:, 0] = S0  # Initial stock price for all simulations

    for i in range(1, n + 1):
        Z = np.random.standard_normal(m)  # Random numbers for simulation
        stock_paths[:, i] = stock_paths[:, i - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return stock_paths
