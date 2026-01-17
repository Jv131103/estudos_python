"""
Faça um programa que:

    Leia uma lista de números

    Remova todos os valores negativos

    Mostre a lista final

Objetivo: remoção + cuidado com iteração.
"""


def remover_negativos_metodo_nova_lista(lista):
    novo = []

    for i in range(len(lista)):
        if lista[i] >= 0:
            novo.append(lista[i])

    return novo


lista = list(range(-10, 11))
print(remover_negativos_metodo_nova_lista(lista[:]))
