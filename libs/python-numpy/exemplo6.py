import numpy as np

# Operações matriciais são cálculos matemáticos específicos,
# Para solucionar sistenas de equações lineares, executar
# tranformações geométricas e realizar análises estatísticas
# multivaloradas de forma mais prática e objetiva.

# Criação de uma matriz 2x2
a = np.array([[1, 2], [3, 4]])

# Transposição de uma matriz, ou seja, inversão de suas linhas
# e colunas
b = a.T
print(f"Transposta da Matriz: {b}")
print()

# Produto matricial
# Diferente da multiplicação direta, elemento a elemento,
# refere-se a uma operação matemática entre duas matrizes,
# com regras específicas, onde os valores da matriz resultante
# são obtidos pela soma dos produtos dos valores correspondentes
# das linhas da primeira matriz e das colunas da segunda matriz
# conforme ilustrado na figura "Formalização do produto matricial"
# Criação de uma matriz 2x2
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Produto matricial entre a e b
c = np.dot(a, b)
print(f"Produto matricial de: {a} e {b}, 1° forma: {c}")

# Ou utilizando o operador @
d = a @ b
print(f"Produto matricial de: {a} e {b}, 2° forma: {c}")

# Valor da matriz c é igual a matriz d
print(c == d)  # Saída: [[ True  True] [ True  True]]
