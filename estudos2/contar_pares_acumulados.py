def contar_pares_acumulados(lista):
    if not lista:
        return []

    cont = 0

    resultado = [0] * len(lista)

    for idx, valor in enumerate(lista):
        if valor % 2 == 0:
            cont += 1

        resultado[idx] = cont

    return resultado


lista = [2, 5, 8, 3, 4, 7]

print(contar_pares_acumulados(lista))
