"""
Faça um programa que:

    Leia uma lista de números

    Crie uma nova lista apenas com os positivos

    Multiplique cada valor por 2

    Use for + if

Não use list comprehension.
"""

lista = [5, -1, 2, -3, -4, 3, 9, 0, 1]
apenas_positivos = []

for valor in lista:
    if valor > 0:
        apenas_positivos.append(valor * 2)

print(apenas_positivos)
