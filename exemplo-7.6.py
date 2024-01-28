import numpy as np

arr = np.array([1, 4, 8, 16, 32])

# Media dos elementos
result = np.mean(arr)
print('Média é:', result)

# Mediana dos elementos
result = np.median(arr)
print('Mediana é: ', result)

# Desvio padrão
result = np.std(arr)
print('Desvio padrão é: ', result)

# Arrays multidimensionais/bidimensional
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Mediana no eixo 0 (linhas)
median_axis0 = np.median(arr, axis=0)
print('Mediana eixo 0: ', median_axis0)

# Mediana no eixo 1 (colunas)
median_axis1 = np.median(arr, axis=1)
print('Medixa eixo 1: ', median_axis1)

median_all = np.median(arr)
print('Mediana de todos os elementos: ', median_all)