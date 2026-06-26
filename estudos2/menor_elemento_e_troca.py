def menor_vai_para_frente(lista):
    if not isinstance(lista, list):
        raise ValueError("Tipo argumento lista só vale para tipo list")

    if not lista:
        return lista

    indice_menor = 0

    for i in range(1, len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i

    lista[0], lista[indice_menor] = lista[indice_menor], lista[0]

    return lista


print(menor_vai_para_frente([7, 2, 8, 1, 9]))
