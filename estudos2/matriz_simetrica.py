def matriz_simetrica(matriz):
    if not matriz:
        return False

    if len(matriz) != len(matriz[0]):
        return False

    for i in range(len(matriz)):
        if len(matriz[i]) != len(matriz):
            return False

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


matriz = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

print(matriz_simetrica(matriz))

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [3, 5, 6]
]

print(matriz_simetrica(matriz))
