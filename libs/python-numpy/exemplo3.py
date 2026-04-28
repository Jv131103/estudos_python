import numpy as np

# Slicing / fatiamento de arrays
# array[inicio:fim:passo]

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Seleção entre a posição 1 e 7, pulando a de 2 em 2.
# Ou seja, nesse caso todos os pares menores que 7.
print(a[1:7:2])  # Saída: [2 4 6]

# Seleção com indexador negativo
# Passo invertido, pulando de 3 em 3.
print(a[::-3])  # Saída: [9 6 3]

b = np.array([
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9]
])

# Seleciona as linhas e colunas pulando de 2 em 2.
# Ou seja, a primeira, segunda e terceira de cada eixo.
print(b[::2, ::2])  # Saída [[1 3 5] [3 5 7] [5 7 9]]
