# NumPy Examples
# Author: Your Name

import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Basic operations
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))

# Reshape
matrix = arr.reshape(5, 1)
print("Reshaped Matrix:\n", matrix)

# Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Dot Product:\n", np.dot(a, b))