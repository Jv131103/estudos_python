"""
Faça uma função recursiva que:

    Receba um número n

    Imprima n até 0

    Pare corretamente

Caso base: n == 0
"""


def contagem_regressiva(n):
    print(n)
    if n == 0:
        return n
    return contagem_regressiva(n - 1)


contagem_regressiva(10)
