def gerar_lista_ponteiros(lista):
    if not lista:
        return []

    resultado = []
    n = len(lista)
    j = 1

    for i in range(n):
        if j == n:
            j = 0
        resultado.append(lista[i] + lista[j])
        j += 1

    return resultado


def gerar_lista_circular(lista):
    if not lista:
        return []

    resultado = []
    n = len(lista)

    for i in range(n - 1):
        resultado.append(lista[i] + lista[i + 1])

    resultado.append(lista[-1] + lista[0])
    return resultado


lista = [1, 2, 3, 4]
print(gerar_lista_circular(lista))
print(gerar_lista_ponteiros(lista))
