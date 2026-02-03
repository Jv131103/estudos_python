"""
Crie uma matriz 3x3 com numpy:

    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

Depois:

    mostre a transposta

    mostre a soma de todos os elementos

    mostre o maior elemento da matriz
"""

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matriz.transpose())
print(matriz.sum())
print(matriz.max())
