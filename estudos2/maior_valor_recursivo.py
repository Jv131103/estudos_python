"""
Faça uma função recursiva que:

    Receba uma lista de números

    Retorne o maior valor

    Sem usar max() nem loop

Dica: compare primeiro elemento com o resto.
"""


def maior_valor_slicing(lista):
    if len(lista) == 1:
        return lista[0]

    maior_do_resto = maior_valor_slicing(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]
    else:
        return maior_do_resto


def maior_valor_manual(lista, i=0):
    if i == len(lista) - 1:
        return lista[i]

    maior_do_resto = maior_valor_manual(lista, i + 1)

    if lista[i] > maior_do_resto:
        return lista[i]
    else:
        return maior_do_resto


lista = [1, 2, 3]
print(maior_valor_slicing(lista))
print(maior_valor_manual(lista))
