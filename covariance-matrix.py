import numpy as np
import pandas as pd

# Create a DataFrame
data = {
    'Study_Hours': [2, 3, 5, 7, 8],
    'Exam_Score': [50, 55, 65, 70, 75]
}

df = pd.DataFrame(data)

# Calculate covariance matrix
cov_matrix = df.cov()
print("Covariance Matrix:\n", cov_matrix)

# Extract covariance between Study_Hours and Exam_Score
cov_xy = cov_matrix.loc['Study_Hours', 'Exam_Score']
print(f"\nCovariance between Study Hours and Exam Score: {cov_xy}")
