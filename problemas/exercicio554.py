"""
Faça um programa que:

    Leia uma lista de números

    Use um set para remover os valores duplicados

    Mostre:

        a lista original

        o conjunto sem duplicatas

        a lista convertida novamente a partir do set

DICAS

    Use set(lista)

    Lembre que a ordem pode mudar

    Compare com uma solução usando lista
"""

lista = [2, 3, 1, 2, 3, 4, 5, 6, 1, 1, 3]
print(f"Lista original: {lista}")

conjunto = set(lista)
print(f"Conjunto sem duplicatas: {conjunto}")

lista = list(conjunto)
print(f"Lista nova sem duplicadas: {lista}")
