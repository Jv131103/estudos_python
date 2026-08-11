def eh_matriz_valida(matriz):
    if not matriz:
        return False

    tamanho = len(matriz[0])

    for linha in matriz:
        if len(linha) != tamanho:
            return False

    return True


def transposta(matriz):
    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    transpor = []

    for coluna in range(0, len(matriz[0])):
        lista = []
        for linha in range(0, len(matriz)):
            lista.append(matriz[linha][coluna])
        transpor.append(lista)

    return transpor


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print(transposta(matriz))
