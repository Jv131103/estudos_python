# Errado
# matriz = [[0] * 3] * 3

# Certo
matriz = [[0] * 3 for _ in range(3)]

matriz[0][0] = 1
print(matriz)
