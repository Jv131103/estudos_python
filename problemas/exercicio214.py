def soma_matriz_recursiva(matriz):
    if not matriz:
        return 0
    return sum(matriz[0]) + soma_matriz_recursiva(matriz[1:])


matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(soma_matriz_recursiva(matriz))
