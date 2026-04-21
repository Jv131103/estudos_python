def lista_ordenada(lista, crescente=True):
    for i in range(1, len(lista)):
        if crescente:
            if lista[i - 1] > lista[i]:
                return False
        else:
            if lista[i - 1] < lista[i]:
                return False
    return True


def quase_ordenada(lista):
    erros = 0

    for i in range(1, len(lista)):
        if lista[i-1] > lista[i]:
            erros += 1
            if erros > 1:
                return False

            if i >= 2 and lista[i-2] > lista[i]:
                lista[i] = lista[i-1]  # ajusta o atual
            else:
                lista[i-1] = lista[i]  # ajusta o anterior

    return True


print(lista_ordenada([1, 2, 3, 4, 5], crescente=True))
print(quase_ordenada([1, 2, 5, 3, 4]))
