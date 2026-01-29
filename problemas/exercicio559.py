"""
Faça um programa que:

    Use random.seed(42)

    Gere 5 números inteiros entre 1 e 10

    Mostre os números gerados

    Execute o programa duas vezes e observe o resultado
"""

import random

# random.seed(42)


def gerar_numeros(qtd):

    lista = []
    for _ in range(qtd):
        lista.append(random.randint(1, 10))

    return " ".join(map(str, lista))


print(gerar_numeros(5))
