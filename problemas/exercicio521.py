"""
Faça um programa que:

    Leia uma lista de números

    Ordene a lista manualmente

    Não use sort() nem sorted()

Dica: bubble sort ou selection sort.
"""


def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return lista


print(selection_sort([64, 25, 12, 22, 11]))
