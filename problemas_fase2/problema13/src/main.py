def somar_matriz(matriz):
    soma_matriz = []

    for linha in range(0, len(matriz)):
        soma = 0
        for coluna in range(0, len(matriz[linha])):
            soma += matriz[linha][coluna]

        soma_matriz.append(soma)

    return soma_matriz


def somar_matriz2(matriz):
    return [sum(linha) for linha in matriz]


def somar_matriz3(matriz):
    soma_matriz = []

    for linha in matriz:
        soma_matriz.append(sum(linha))

    return soma_matriz


def soma_pa(linha):
    n = len(linha)
    return n * (linha[0] + linha[-1]) // 2


def somar_matriz4(matriz):
    soma_matriz = []

    for linhas in matriz:
        soma_matriz.append(soma_pa(linhas))

    return soma_matriz


if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matriz = [[5, 7, 9], [7, 9, 12], [3, 5, 7]]

    print(somar_matriz(matriz))
    print(somar_matriz2(matriz))
    print(somar_matriz3(matriz))
    print(somar_matriz4(matriz))
