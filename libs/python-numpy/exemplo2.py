import numpy as np

# Acesso a elementos de um array com numpy
a = np.array([1, 4, 3, 7, 2, 0, 7, 3, 5])
b = np.array([[1, 4, 3], [7, 2, 0], [7, 3, 5]])

# Verifica o formato das matrizes
print(a.shape, b.shape)  # Saída: (9,) (3, 3)

# Acesso a elementos únicos e sequenciais
print(a[0])  # Saída: 1
print(a[1:3])  # Saída: [4 3]

# Acesso à arrays bidimensionais
print(b[0])  # Saída: [1 4 3]
print(b[1, 1])  # Saída: 2

# Modificação do elemento na posição 0
a[0] = 10
print(a)  # Saída: [10 4 3 7 2 0 7 3 5]

# Modificação do elemento na posição central da matriz 3x3
b[1][1] = 10
print(b)
# Saída:
# [[1 4  3]
#  [7 10 0]
#  [7 3  5]]
