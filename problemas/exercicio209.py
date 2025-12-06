def contar_elementos(lista, alvo):
    if not lista:
        return 0

    if lista[0] == alvo:
        return 1 + contar_elementos(lista[1:], alvo)
    else:
        return contar_elementos(lista[1:], alvo)


lista = [1, 2, 3, 2, 4, 2]
print(contar_elementos(lista, 2))
