"""
Faça um programa que:

    Receba uma lista de números

    Remova todos os números pares in place

    Não crie uma nova lista

    Não use filter, list comprehension ou remove dentro de loop for

Dica:

    Use while

    Pense no impacto da remoção nos índices
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0

while i < len(lista):
    if lista[i] % 2 == 0:
        lista.pop(i)
    else:
        i += 1


print(lista)
