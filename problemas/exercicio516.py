"""
Faça um programa que:

    Leia uma lista de números

    Crie duas listas:

        uma com números pares

        outra com números ímpares

    Mostre ambas

Objetivo: condicional + listas.
"""

from random import randint

lista = []

limite = randint(5, 20)
for _ in range(limite):
    lista.append(randint(0, 1000))


lista_pares = []
lista_impares = []

for dados in lista:
    if (dados & 1) == 0:
        lista_pares.append(dados)
    else:
        lista_impares.append(dados)


print(f"Lista Original: {lista}")
print(f"Lista Pares: {lista_pares}")
print(f"Lista Ímpares: {lista_impares}")
