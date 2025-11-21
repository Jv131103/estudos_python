def copia_lista(lista):
    if not isinstance(lista, list):
        return None

    nova_lista = []
    for i in lista:
        nova_lista.append(i)
    return nova_lista


lista = [1, 2, 3]
nova_lista = copia_lista(lista)
print(lista == nova_lista)
