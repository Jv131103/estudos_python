def segundo_maior(lista):
    if not isinstance(lista, list):
        raise ValueError("Parametro lista precisa ser do tipo list")

    if not lista:
        return lista

    if lista[0] > lista[1]:
        maior = lista[0]
        segundo_maior = lista[1]
    else:
        maior = lista[1]
        segundo_maior = lista[0]

    for num in lista:
        if num > maior:
            segundo_maior = maior
            maior = num
        elif num > segundo_maior and num != maior:
            segundo_maior = num

    if segundo_maior == maior:
        return None

    return segundo_maior


def segundo_maior_ordenado(lista):
    ordenada = sorted(lista)
    return ordenada[-2] if ordenada[-2] != ordenada[-1] else None


def segundo_maior_ordenado2(lista):
    lista.sort()
    return lista[-2] if lista[-2] != lista[-1] else None


if __name__ == "__main__":
    lista = [5, 5, 4, 4, 1]
    print(segundo_maior(lista))
    print(segundo_maior_ordenado(lista))
    print(segundo_maior_ordenado2(lista.copy()))
