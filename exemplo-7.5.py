import numpy as np

arr1 = np.array([[1, 2,], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Concatenação de arrays na vertical/horizontal
result = np.concatenate((arr1, arr2), axis=0) # linhas
print(result)

result = np.concatenate((arr1, arr2), axis=1) # colunas
print(result)

# Concatenação de arrays em vetor
result = np.concatenate((arr1, arr2), axis=None) # vetor
print(result)

# Transposição de um array
result = arr1.T
print(result)
