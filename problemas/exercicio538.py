"""
Faça um programa que:

    Receba uma lista de números

    Faça um shift à esquerda de 1 posição

    O último elemento deve virar 0

    O primeiro elemento deve ser descartado

    A modificação deve ser feita in place

Exemplo:

    Entrada:  [5, 6, 7, 8]
    Saída:    [6, 7, 8, 0]
"""


def shift_esquerda(lista):
    n = len(lista)

    # começa do fim para não sobrescrever valores
    for i in range(0, n - 1):
        lista[i] = lista[i + 1]

    lista[-1] = 0  # valor novo entra no começo

    return lista


print(shift_esquerda([5, 6, 7, 8]))
