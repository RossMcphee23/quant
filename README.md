# European Option Pricing Simulation using Monte Carlo Method

This project simulates stock price paths using the Monte Carlo method and estimates the price of a European option (either a call or put) based on those simulations. The 
simulation follows the Black-Scholes model for stock price evolution and calculates the option payoff at maturity. The final option price is obtained by averaging the 
discounted payoffs across all simulations.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
- [Output](#output)
- [Example Output](#example-output)
- [Documentation](#documentation)
- [References](#references)

## Overview
This code simulates stock price paths using geometric Brownian motion. It then calculates the payoff for a European option at maturity based on these simulated prices. 
Finally, it estimates the option's price by averaging the discounted payoffs across all simulations.

## Installation
1. Ensure you have Python installed (version 3.x).
2. Install the required libraries using:
   ```bash
   pip install numpy matplotlib

## Usage 
In the file 'main.py' file there is an option to manipulate initial parameters, and actively see how this affects the market.
