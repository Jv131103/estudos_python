"""
Faça um programa que:

    Receba uma lista de números

    Faça um shift à direita de 1 posição

    O primeiro elemento deve virar 0

    O último elemento deve ser descartado

    A modificação deve ser feita in place

Exemplo:

    Entrada:  [1, 2, 3, 4]
    Saída:    [0, 1, 2, 3]
"""


def shift_direita(lista):
    n = len(lista)

    # começa do fim para não sobrescrever valores
    for i in range(n - 1, 0, -1):
        lista[i] = lista[i - 1]

    lista[0] = 0  # valor novo entra no começo

    return lista


print(shift_direita([1, 2, 3, 4]))
