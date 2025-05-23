import pandas as pd
import numpy as np

# Define the file path to the input data
data_path = 'E:\\network\\du\\tong2.0\\shangquanfa_2.0cutA.csv'

# Read the CSV data into a DataFrame
data = pd.read_csv(data_path)

# 1. Min-max normalization (scale data to [0, 1] range)
normalized_data = (data - data.min()) / (data.max() - data.min())
print("Normalized data:")
print(normalized_data.head())  # Display the first few rows of normalized data

# 2. Calculate the proportion p_ij for each indicator
p = normalized_data.div(normalized_data.sum(axis=0), axis=1)
print("Proportion values p_ij for each indicator:")
print(p.head())  # Display the first few rows of proportion values

# 3. Calculate the entropy value e_j for each indicator
n = len(data)  # Number of samples
k = 1 / np.log(n)
entropy = -k * (p * np.log(p + 1e-6)).sum()  # Add small value to avoid log(0)
print("Entropy values e_j for each indicator:")
print(entropy)  # Print entropy for each column

# 4. Adjust entropy values (you can apply other adjustments here if needed)
adjusted_entropy = entropy.copy()  # In this case, no further adjustment
print("Adjusted entropy values:")
print(adjusted_entropy)

# 5. Calculate weights (1 - e_j) and normalize to ensure weights sum to 1
total_entropy = adjusted_entropy.sum()
weights = (1 - adjusted_entropy) / (len(adjusted_entropy) - total_entropy)
print("Initial weight calculation:")
print(weights)

# Normalize the weights to make sure they sum to 1
weights = weights / weights.sum()
print("Normalized weights:")
print(weights)

# Final output
print("Final weights for each indicator:")
print(weights)
