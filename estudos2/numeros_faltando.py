def faltando(lista, n):
    for valor in range(1, n + 1):
        if valor not in lista:
            return valor

    return None


def faltando_matematico(lista, n):
    calculo = n * (n + 1) // 2

    soma_lista = 0
    for valor in lista:
        soma_lista += valor

    if soma_lista != calculo:
        return calculo - soma_lista
    return None


def adicionar_faltando(lista, n):
    faltante = faltando_matematico(lista, n)

    if faltante is None:
        return lista.copy()

    novo = []

    for v in lista:
        if faltante < v and faltante not in novo:
            novo.append(faltante)

        novo.append(v)

    if faltante not in novo:
        novo.append(faltante)

    return novo


lista = [1, 2, 3, 5, 6]
n = 6
print(faltando(lista, n))
print(faltando_matematico(lista, n))
print(adicionar_faltando(lista, n))
