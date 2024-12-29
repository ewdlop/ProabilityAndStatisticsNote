import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Define population parameters
population_size = 100000
lambda_param = 1/10  # Mean = 10

# Generate an exponential distribution population
population = np.random.exponential(scale=1/lambda_param, size=population_size)

# Parameters for sampling
sample_size = 50
num_samples = 1000
sample_means = []

# Take samples and compute means
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size, replace=False)
    sample_mean = np.mean(sample)
    sample_means.append(sample_mean)

# Convert to NumPy array for convenience
sample_means = np.array(sample_means)

# Plot the population distribution
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(population, bins=100, kde=True, color='skyblue')
plt.title('Population Distribution (Exponential)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot the distribution of sample means
plt.subplot(1, 2, 2)
sns.histplot(sample_means, bins=30, kde=True, color='salmon')
plt.title('Distribution of Sample Means (n=50)')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Theoretical Mean and Standard Error
theoretical_mean = 1 / lambda_param  # Mean of exponential distribution
theoretical_se = (1 / lambda_param) / np.sqrt(sample_size)

print(f"Theoretical Mean: {theoretical_mean}")
print(f"Theoretical Standard Error: {theoretical_se}")

# Sample Mean and Standard Deviation of Sample Means
empirical_mean = np.mean(sample_means)
empirical_std = np.std(sample_means)

print(f"\nEmpirical Mean of Sample Means: {empirical_mean:.2f}")
print(f"Empirical Standard Deviation of Sample Means: {empirical_std:.2f}")
