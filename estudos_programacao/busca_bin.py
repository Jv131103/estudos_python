def busca_bin(lista, valor):
    lista.sort()

    e = 0
    d = len(lista) - 1

    while e <= d:
        meio = (e + d) // 2

        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            e = meio + 1
        elif lista[meio] > valor:
            d = meio - 1

    return -1


print(busca_bin(list(range(100)), 25))
print(busca_bin([10, 31, 0, 9, 7, 21, 34, 22, 19, -1], 9))
