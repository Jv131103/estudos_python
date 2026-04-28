import numpy as np

print(np.ndarray)

# Array unidimensional a partir de uma lista
a = np.array([1, 4, 3, 7, 2, 0, 7, 3, 5])
print(a)
print()

# Array bidimensional a partir de uma lista
b = np.array([[1, 4, 3], [7, 2, 0], [7, 3, 5]])
print(b)
print()

# Array com 3 linhas e 4 colunas
# Preenchido com números zero
c = np.zeros((3, 4))
print(c)
print()

# Array com 2 linhas e 3 colunas
# Preenchido com números um
d = np.ones((2, 3))
print(d)
print()

# Array com 2 linhas e 2 colunas
# Preenchido com valores aleatórios entre 0 e 1
e = np.random.random((2, 2))
print(e)
print()

# Array com uma sequência de números
e = np.arange(0, 10, 2)
print(e)
print()

# Array com valores espaçados linearmente
f = np.linspace(0, 1, 5)
print(f)
print()


