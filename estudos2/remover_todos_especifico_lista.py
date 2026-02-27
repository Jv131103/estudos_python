def remover_todos_especificos_inplace(lista, dado):
    if not isinstance(lista, list):
        raise TypeError("lista precisa ser do tipo list")

    i = 0

    while i <= len(lista) - 1:
        if lista[i] == dado:
            lista.pop(i)
        else:
            i += 1

    return lista


def remover_todos_especificos_inplace2(lista, dado):
    if not isinstance(lista, list):
        raise TypeError("lista precisa ser do tipo list")

    write = 0

    for read in range(len(lista)):
        if lista[read] != dado:
            lista[write] = lista[read]
            write += 1

    del lista[write:]
    return lista


def remover_todos_especificos_novalista(lista, dado):
    if not isinstance(lista, list):
        raise TypeError("lista precisa ser do tipo list")

    novo = []

    for valor in lista:
        if valor != dado:
            novo.append(valor)

    return novo


def remover_todos_especificos_novalista2(lista, dado):
    if not isinstance(lista, list):
        raise TypeError("lista precisa ser do tipo list")

    return [x for x in lista if x != dado]


def remover_todos_especificos_novalista3(lista, dado):
    if not isinstance(lista, list):
        raise TypeError("lista precisa ser do tipo list")

    return list(filter(lambda i: i != dado, lista))


print(remover_todos_especificos_inplace([1, 2, 3, 5, 4, 3], 3))
print(remover_todos_especificos_inplace([3, 3, 3, 3, 3, 3], 3))
print(remover_todos_especificos_inplace([1, 2, 3, 5, 4, 3, 2], 3))
print(remover_todos_especificos_inplace([1, 2, 9, 5, 4, 3, 2], 3))
print(remover_todos_especificos_inplace([1, 2, 9, 5, 4, 2], 3))
print(remover_todos_especificos_inplace([], 3))
print()
print(remover_todos_especificos_inplace2([1, 2, 3, 5, 4, 3], 3))
print(remover_todos_especificos_inplace2([3, 3, 3, 3, 3, 3], 3))
print(remover_todos_especificos_inplace2([1, 2, 3, 5, 4, 3, 2], 3))
print(remover_todos_especificos_inplace2([1, 2, 9, 5, 4, 3, 2], 3))
print(remover_todos_especificos_inplace2([1, 2, 9, 5, 4, 2], 3))
print(remover_todos_especificos_inplace2([], 3))
print()
print(remover_todos_especificos_novalista([1, 2, 3, 5, 4, 3], 3))
print(remover_todos_especificos_novalista([3, 3, 3, 3, 3, 3], 3))
print(remover_todos_especificos_novalista([1, 2, 3, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista([1, 2, 9, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista([1, 2, 9, 5, 4, 2], 3))
print(remover_todos_especificos_novalista([], 3))
print()
print(remover_todos_especificos_novalista2([1, 2, 3, 5, 4, 3], 3))
print(remover_todos_especificos_novalista2([3, 3, 3, 3, 3, 3], 3))
print(remover_todos_especificos_novalista2([1, 2, 3, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista2([1, 2, 9, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista2([1, 2, 9, 5, 4, 2], 3))
print(remover_todos_especificos_novalista2([], 3))
print()
print(remover_todos_especificos_novalista3([1, 2, 3, 5, 4, 3], 3))
print(remover_todos_especificos_novalista3([3, 3, 3, 3, 3, 3], 3))
print(remover_todos_especificos_novalista3([1, 2, 3, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista3([1, 2, 9, 5, 4, 3, 2], 3))
print(remover_todos_especificos_novalista3([1, 2, 9, 5, 4, 2], 3))
print(remover_todos_especificos_novalista3([], 3))
