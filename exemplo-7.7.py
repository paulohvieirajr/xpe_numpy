import numpy as np


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Multiplicação
result = np.dot(arr1, arr2)
print(result)

# Determinante
arr = np.array([[1, 2], [3, 4]])
result = np.linalg.det(arr)
print(result)
