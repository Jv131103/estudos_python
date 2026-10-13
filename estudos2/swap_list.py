def swap(lista, i, j):
    if not lista:
        raise ValueError("Lista não pode ser vazia")

    if i < 0 or i >= len(lista):
        raise IndexError("Índice i inválido")

    if j < 0 or j >= len(lista):
        raise IndexError("Índice j inválido")

    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp

    return lista


lista = [10, 20, 30, 40]
swap(lista, 1, 3)

print(lista)

lista = [5, 10, 15, 20, 25]
swap(lista, 1, 3)
swap(lista, 0, 4)
print(lista)
