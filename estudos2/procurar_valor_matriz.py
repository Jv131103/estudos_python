def procurar_valor_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor:
                return i, j

    return (-1, -1)


def procurar_matriz_eficiente(matriz, valor):
    if not matriz or not matriz[0]:
        return (-1, -1)

    linha = 0
    coluna = len(matriz[0]) - 1  # Começa no canto superior direito

    while linha < len(matriz) and coluna >= 0:
        atual = matriz[linha][coluna]

        if atual == valor:
            return (linha, coluna)
        elif atual > valor:
            coluna -= 1  # O valor é menor, elimina a coluna e vai para a esquerda
        else:
            linha += 1  # O valor é maior, elimina a linha e vai para baixo

    return (-1, -1)


# Se a matriz for ordenada
def procurar_matriz_binaria(matriz, valor):
    if not matriz:
        return (-1, -1)

    linhas = len(matriz)
    colunas = len(matriz[0])

    inicio = 0
    fim = (linhas * colunas) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # A mágica da conversão de índice linear para (linha, coluna)
        r = meio // colunas
        c = meio % colunas

        if matriz[r][c] == valor:
            return (r, c)
        elif matriz[r][c] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return (-1, -1)


matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(procurar_valor_matriz(matriz, 50))
print(procurar_valor_matriz(matriz, 15))
print(procurar_matriz_eficiente(matriz, 50))
print(procurar_matriz_eficiente(matriz, 15))
print(procurar_matriz_binaria(matriz, 50))
print(procurar_matriz_binaria(matriz, 15))
