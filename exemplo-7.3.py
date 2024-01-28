import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acessando indice basico 
print(arr1[0])

# Acessando fatias no vetor
print(arr1[1:4])

# Acessando elementos a partir do final
print(arr1[-1])

# Acessando elementos do array multidimensional
print(arr2[0])
print(arr2[1, 0])

