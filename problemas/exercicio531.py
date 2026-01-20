"""
Faça um programa que:

    Receba uma lista de números

    Use slicing para criar:

        uma lista com os elementos em posições pares

        uma lista com os elementos em posições ímpares

    Mostre ambas as listas

Use apenas slicing ([::]).
Não use for, while ou enumerate.
"""

lista = list(range(0, 101))

pares = lista[0::2]
print(pares)

impares = lista[1::2]
print(impares)
