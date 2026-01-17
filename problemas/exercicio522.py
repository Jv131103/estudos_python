"""
Faça um programa que:

    Receba uma lista que pode conter listas

    Some todos os números

    Use recursão ou loop com recursão
"""


def somar(matriz):
    soma = 0
    for valores in matriz:
        if isinstance(valores, list):
            soma += somar(valores)
        else:
            soma += valores

    return soma


matriz = [1, [2, [3, 4]], 5]
print(somar(matriz))
