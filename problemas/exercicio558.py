"""
Faça um programa que:

    Leia uma lista de números

    Remova todos os valores iguais a 0

    Faça isso in place

    Não crie uma nova lista auxiliar

Exemplo conceitual:

    [0, 1, 0, 3, 0, 5] → [1, 3, 5]

DICAS

    Use dois ponteiros:

        fast percorre a lista

        slow marca a próxima posição válida

    Quando lista[fast] != 0, copie para lista[slow]

    Ao final, corte a lista até slow
"""


def remove_zeros(lista):
    if not lista:
        return None

    slow = 0
    fast = 0

    while fast < len(lista):
        if lista[fast] != 0:
            lista[slow] = lista[fast]
            slow += 1
        fast += 1

    del lista[slow:]

    return lista


print(remove_zeros([0, 1, 0, 3, 0, 5]))
print(remove_zeros([1, 0, 0, 3, 0, 5]))
print(remove_zeros([1, 0, 0, 3, 0, 5, 9, 1, 0]))
