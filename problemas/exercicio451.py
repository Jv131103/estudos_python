"""
Faça um programa que:

    Leia uma lista de números

    Ordene a lista manualmente usando swap

    Não use sort() nem sorted()

Dica: pense em bubble ou selection sort.
"""

lista = [3, 2, 4, 5, 9, 9, 0]

n = len(lista)

for i in range(n):
    for j in range(n - 1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista)
