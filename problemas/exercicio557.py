"""
Faça um programa que:

    Leia uma lista de números

    Inverta a lista in place

    Use dois ponteiros

Não use:

    reverse()

    slicing ([::-1])

Exemplo conceitual:

    [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]

"""


def reverse_list(lista):
    if not lista:
        return None

    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro < ultimo:
        lista[primeiro], lista[ultimo] = lista[ultimo], lista[primeiro]
        primeiro += 1
        ultimo -= 1

    return lista


lista = [1, 2, 3, 4, 5]
print(reverse_list(lista))
