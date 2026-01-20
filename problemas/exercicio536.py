"""
Faça um programa que:

    Receba uma lista de números inteiros

    Reorganize a lista in place de forma que:

        todos os números negativos fiquem à esquerda

        todos os números maiores ou iguais a zero fiquem à direita

        A ordem interna não importa

        Não crie uma nova lista

        Não use sort() nem sorted()
"""


def organizar(lista):
    i = 0
    j = len(lista) - 1

    while i <= j:
        if lista[i] < 0:
            i += 1
        else:
            lista[i], lista[j] = lista[j], lista[i]
            j -= 1

    return lista


print(organizar([-1, 0, 2, 3, -2]))
