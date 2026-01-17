def busca_binaria(lista, valor):
    lista = sorted(lista)

    inicio = 0

    fim = len(lista) - 1

    while inicio <= fim:

        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio

        if lista[meio] < valor:
            inicio = meio + 1
        elif lista[meio] > valor:
            fim = meio - 1

    return -1


def busca_binaria_recursiva(lista, valor, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2
    if lista[meio] == valor:
        return meio
    elif lista[meio] < valor:
        return busca_binaria_recursiva(lista, valor, meio + 1, fim)
    else:
        return busca_binaria_recursiva(lista, valor, inicio, meio - 1)


lista = [1, 3, 5, 7, 9, 11]

print(busca_binaria(lista, 7))
print(busca_binaria(lista, 4))

print()

print(busca_binaria_recursiva(lista, 7))
print(busca_binaria_recursiva(lista, 4))
