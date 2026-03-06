def posicao_circular_mathversion(lista, i):
    if i >= len(lista):
        return None

    indice = (i + 1) % len(lista)
    return lista[i] + lista[indice]


def posicao_circular_ifversion(lista, i):
    if i >= len(lista):
        return None

    indice = i + 1

    if indice == len(lista):
        indice = 0

    return lista[i] + lista[indice]


def posicao_circular_whileversion(lista, i):
    if i >= len(lista):
        return None

    indice = i + 1

    while indice >= len(lista):
        indice -= len(lista)

    return lista[i] + lista[indice]


def posicao_circular_ternario(lista, i):
    if i >= len(lista):
        return None

    indice = 0 if i + 1 == len(lista) else i + 1
    return lista[i] + lista[indice]


def posicao_circular_try(lista, i):
    if i >= len(lista):
        return None

    try:
        return lista[i] + lista[i + 1]
    except IndexError:
        return lista[i] + lista[0]


def gerar_lista_inplace(lista, function_circle):
    posic_inicial, posic_final = lista[0], lista[-1]
    for i in range(0, len(lista) - 1):
        lista[i] = function_circle(lista, i)

    lista[-1] = posic_final + posic_inicial
    return lista


def gerar_lista_nao_inplace(lista, function_circle):
    resultado = []

    for i in range(0, len(lista)):
        resultado.append(function_circle(lista, i))

    return resultado


def gerar_lista_nao_inplace2(lista, function_circle):
    return [function_circle(lista, i) for i in range(len(lista))]


if __name__ == "__main__":
    lista = [2, 4, 3]  # [1, 2, 3, 4]
    print(gerar_lista_inplace(lista.copy(), posicao_circular_mathversion))
    print(gerar_lista_inplace(lista.copy(), posicao_circular_ifversion))
    print(gerar_lista_inplace(lista.copy(), posicao_circular_whileversion))
    print(gerar_lista_inplace(lista.copy(), posicao_circular_ternario))
    print(gerar_lista_inplace(lista.copy(), posicao_circular_try))
    print(gerar_lista_nao_inplace(lista.copy(), posicao_circular_mathversion))
    print(gerar_lista_nao_inplace(lista.copy(), posicao_circular_ifversion))
    print(gerar_lista_nao_inplace(lista.copy(), posicao_circular_whileversion))
    print(gerar_lista_nao_inplace(lista.copy(), posicao_circular_ternario))
    print(gerar_lista_nao_inplace(lista.copy(), posicao_circular_try))
    print(gerar_lista_nao_inplace2(lista.copy(), posicao_circular_mathversion))
    print(gerar_lista_nao_inplace2(lista.copy(), posicao_circular_ifversion))
    print(gerar_lista_nao_inplace2(lista.copy(), posicao_circular_whileversion))
    print(gerar_lista_nao_inplace2(lista.copy(), posicao_circular_ternario))
    print(gerar_lista_nao_inplace2(lista.copy(), posicao_circular_try))
