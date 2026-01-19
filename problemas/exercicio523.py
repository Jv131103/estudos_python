"""
Faça um programa que:

    Receba uma lista de números inteiros

    Modifique a lista in place

    Substitua todos os valores negativos por 0

    Mostre a lista final

Regras:

    Não crie uma nova lista

    Use índices para modificar os elementos
"""

lista = [1, 3, -1, 2, 0, -4, 8, 9, -9]

for i in range(len(lista)):
    if lista[i] < 0:
        lista[i] = 0

print(lista)
