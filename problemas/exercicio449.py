"""
Faça um programa que:

    Leia uma lista de 5 números

    Troque o primeiro com o último elemento

Mostre a lista final
"""

lista = list(range(5))

print(lista)

temp = lista[0]
lista[0] = lista[len(lista) - 1]
lista[len(lista) - 1] = temp

print(lista)
