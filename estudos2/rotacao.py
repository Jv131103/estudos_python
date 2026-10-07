def rotacionar_direita_com_slicing(lista, k):
    if not lista:
        return []

    k = k % len(lista)

    if k == 0:
        return lista.copy()

    final = lista[-k:]
    inicio = lista[:-k]

    return final + inicio


def rotacionar_direita_sem_slicing(lista, k):
    if not lista:
        return []

    k = k % len(lista)

    resultado = []

    # Adiciona os últimos k elementos
    inicio_rotacao = len(lista) - k

    for i in range(inicio_rotacao, len(lista)):
        resultado.append(lista[i])

    # Adiciona o restante
    for i in range(0, inicio_rotacao):
        resultado.append(lista[i])

    return resultado


def rotacionar_direita_por_vez(lista, k):
    if not lista:
        return []

    k = k % len(lista)

    for _ in range(k):
        ultimo = lista[-1]

        for i in range(len(lista) - 1, 0, -1):
            lista[i] = lista[i - 1]

        lista[0] = ultimo

    return lista


lista = [1, 2, 3, 4, 5]

print(rotacionar_direita_com_slicing(lista, 2))
print(rotacionar_direita_sem_slicing(lista, 2))
print(rotacionar_direita_por_vez(lista, 2))
