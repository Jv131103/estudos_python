def remover_posicoes_pares_lista(lista):
    lista_nova = []

    for i in range(len(lista)):
        if i % 2 != 0:
            lista_nova.append(lista[i])

    return lista_nova


print(remover_posicoes_pares_lista(['a', 'b', 'c', 'd', 'e', 'f']))
