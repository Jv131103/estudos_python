def transpor_matriz(matriz):
    if not matriz:
        return []

    transposta = []
    for i in range(len(matriz[0])):
        novo = []
        for j in range(len(matriz)):
            novo.append(matriz[j][i])
        transposta.append(novo)

    return transposta


print(transpor_matriz([[1, 2, 3], [4, 5, 6]]))
print(transpor_matriz([[1, 2], [3, 4]]))
print(transpor_matriz([]))
