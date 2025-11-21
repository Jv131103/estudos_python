def existe_ao_menos_um_igual(lista1, lista2, elemento):
    return elemento in lista1 and elemento in lista2


def existe_ao_menos_um_igual2(lista1, lista2, elemento):
    existe_na_lista1 = False
    existe_na_lista2 = False

    for i in lista1:
        if i == elemento:
            existe_na_lista1 = True

    for i in lista2:
        if i == elemento:
            existe_na_lista2 = True

    return existe_na_lista1 and existe_na_lista2


def existe_ao_menos_um_igual3(lista1, lista2, elemento):
    for i in lista1:
        for j in lista2:
            if i == j == elemento:
                return True
    return False


lista1 = [1, 2, 3]
lista2 = [3, 4, 5]
print(existe_ao_menos_um_igual(lista1, lista2, 3))
print(existe_ao_menos_um_igual2(lista1, lista2, 3))
print(existe_ao_menos_um_igual3(lista1, lista2, 3))
print()
print(existe_ao_menos_um_igual2(lista1, lista2, 1))
print(existe_ao_menos_um_igual2(lista1, lista2, 1))
print(existe_ao_menos_um_igual3(lista1, lista2, 1))
