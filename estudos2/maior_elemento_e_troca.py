def maior_vai_para_cima(lista):
    if not isinstance(lista, list):
        raise ValueError("Tipo argumento lista só vale para tipo list")

    if not lista:
        return lista

    indice_maior = 0

    for i in range(1, len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i

    lista[indice_maior], lista[-1] = lista[-1], lista[indice_maior]

    return lista


print(maior_vai_para_cima([4, 8, 2, 7, 5]))
