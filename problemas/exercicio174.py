def verificar_ordenada_crescente(lista):
    antes = lista[0]

    for valores in lista:
        if antes > valores:
            return False
        antes = valores
    return True


def verificar_ordenada_decrescente(lista):
    antes = lista[0]

    for valores in lista:
        if valores > antes:
            return False
        antes = valores

    return True


def lista_esta(lista):
    if not lista:
        return "Vazia"

    if not isinstance(lista, list):
        return "Tipo Icompatível"

    if verificar_ordenada_crescente(lista):
        return "Crescente"
    elif verificar_ordenada_decrescente(lista):
        return "Decrescente"
    else:
        return "Desordenada"


listas = [
    [1, 2, 3, 4],
    [1, 3, 5, 7],
    [1, 6, 5, 7],
    [10, 8, 5, 1],
    [5, 4, 3, 2, 1],
    [],
    [0, 0, 0, 0, 0, 0],
    [1, 5, 3, 7],
    ""
]

for lista in listas:
    print(f"Resultado da lista {lista}: {lista_esta(lista)}")
