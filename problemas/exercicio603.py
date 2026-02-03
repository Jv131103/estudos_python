"""
Crie dois arrays:

    a = [1, 2, 3]
    b = [4, 5, 6]

Calcule:

    soma dos arrays

    multiplicação dos arrays

    subtração dos arrays

Tudo usando operações do numpy (sem for).
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"Soma: {a + b}")
print(f"Multiplicação: {a * b}")
print(f"Subtração: {a - b}")
