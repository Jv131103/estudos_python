def compactar(lista):
    if not lista:
        return []

    lista_final = []

    antes = lista[0]
    i = 1
    cont = 1
    while i < len(lista):
        if lista[i] == antes:
            cont += 1
        else:
            lista_final.append([antes, cont])
            cont = 1
        antes = lista[i]
        i += 1

    lista_final.append([antes, cont])

    return lista_final


def compactar2(lista):
    if not lista:
        return []

    i = 0

    lista_contagem = []
    valor = []
    cont = 1
    for j in range(1, len(lista)):
        if lista[i] == lista[j]:
            cont += 1
        else:
            valor.append(lista[i])
            lista_contagem.append(cont)
            cont = 1

        i += 1

    valor.append(lista[i])
    lista_contagem.append(cont)

    final = []
    for v, c in zip(valor, lista_contagem):
        final.append([v, c])

    return final


def compactar_com_pilha(lista):
    if not lista:
        return []

    resultado = []
    pilha = []

    for valor in lista:
        if not pilha or valor == pilha[-1]:
            pilha.append(valor)

        else:
            valor_anterior = pilha[-1]
            contador = 0

            while pilha:
                pilha.pop()
                contador += 1

            resultado.append([valor_anterior, contador])

            pilha.append(valor)

    # processa o último grupo
    if pilha:
        valor_anterior = pilha[-1]
        contador = 0

        while pilha:
            pilha.pop()
            contador += 1

        resultado.append([valor_anterior, contador])

    return resultado


lista = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3]
print(compactar([1, 1, 1, 2, 2, 5, 5, 5, 5, 3]))
print(compactar([1, 1, 2, 1, 1]))
print(compactar([7]))
print(compactar([]))
print()
print(compactar2([1, 1, 1, 2, 2, 5, 5, 5, 5, 3]))
print(compactar2([1, 1, 2, 1, 1]))
print(compactar2([7]))
print(compactar2([]))
print()
print(compactar_com_pilha([1, 1, 1, 2, 2, 5, 5, 5, 5, 3]))
print(compactar_com_pilha([1, 1, 2, 1, 1]))
print(compactar_com_pilha([7]))
print(compactar_com_pilha([]))
