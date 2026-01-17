"""
Faça um programa que:

    Leia uma lista

    Inverta a lista

    Use swap

Objetivo: controle de índices.
"""

lista = ['a', 'b', 'c', 'd', 'e']


def inversao1(lista):
    if not lista:
        return None

    novo = []
    for i in range(len(lista) - 1, -1, -1):
        novo.append(lista[i])

    return novo


def inversao2(lista):
    if not lista:
        return None

    i = 0
    j = len(lista) - 1

    while i <= j:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
        i += 1
        j -= 1

    return lista


def inversao3(lista):
    if not lista:
        return None
    return lista[::-1]


def inversao4(lista):
    if not lista:
        return None
    return list(reversed(lista))


print(inversao1(lista[:]))
print(inversao2(lista[:]))
print(inversao3(lista[:]))
print(inversao4(lista[:]))
