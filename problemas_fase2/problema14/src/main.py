def eh_matriz_valida(matriz):
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


def transposta2(matriz):

    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    linhas = len(matriz)
    colunas = len(matriz[0])

    transposta = []

    for col in range(colunas):
        nova_linha = []

        for lin in range(linhas):
            nova_linha.append(matriz[lin][col])

        transposta.append(nova_linha)

    return transposta


def transposta3(matriz):
    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    return [list(coluna) for coluna in zip(*matriz)]


def transposta4(matriz):
    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    return [
        [matriz[lin][col] for lin in range(len(matriz))]
        for col in range(len(matriz[0]))
    ]


def transposta5(matriz):
    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    linhas = len(matriz)
    colunas = len(matriz[0])

    resultado = [[0] * linhas for _ in range(colunas)]

    for lin in range(linhas):
        for col in range(colunas):
            resultado[col][lin] = matriz[lin][col]

    return resultado


def transposta6(matriz, col=0):
    if not eh_matriz_valida(matriz):
        raise ValueError("matriz irregular")

    if col == len(matriz[0]):
        return []

    coluna_atual = [linha[col] for linha in matriz]
    return [coluna_atual] + transposta6(matriz, col + 1)


if __name__ == "__main__":

    matriz = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transposta(matriz))
    print(transposta2(matriz))
    print(transposta3(matriz))
    print(transposta4(matriz))
    print(transposta5(matriz))
    print(transposta6(matriz))
