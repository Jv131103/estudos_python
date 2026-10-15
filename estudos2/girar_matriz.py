def girar_matriz(matriz):
    if not matriz:
        return []

    giro = []

    for i in range(len(matriz[0])):
        novo = []

        for j in range(len(matriz) - 1, -1, -1):
            novo.append(matriz[j][i])

        giro.append(novo)

    return giro


def girar_matriz_roubado(matriz):
    giro = []
    for i in range(len(matriz[0])):
        novo = []
        for j in range(len(matriz)):
            novo.append(matriz[j][i])
        giro.append(novo[::-1])

    return giro


print(girar_matriz([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(girar_matriz([
    [1, 2, 3],
    [4, 5, 6]
]))
