def soma_linha_recursiva(linha):
    if not linha:
        return 0
    return linha[0] + soma_linha_recursiva(linha[1:])


def soma_matriz_recursiva(matriz):
    if not matriz:
        return 0

    primeira_linha = matriz[0]
    resto = matriz[1:]

    return soma_linha_recursiva(primeira_linha) + soma_matriz_recursiva(resto)


matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(soma_matriz_recursiva(matriz))
