"""
Faça um programa que:

    Crie uma lista de números de 1 a 10

    Embaralhe a lista usando random.shuffle

    Mostre a lista antes e depois
"""

import random


def embaralhar(lista):
    random.shuffle(lista)


lista = list(range(1, 11))
print(f"Antes: {lista}")

embaralhado = embaralhar(lista)
print(f"Depois: {lista}")
