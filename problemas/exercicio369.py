def gerar_lista_alternada(limite):
    lista_alternada = []
    for valor in range(1, limite):
        if valor & 1 == 0:
            lista_alternada.append(-valor)
        else:
            lista_alternada.append(valor)
    return lista_alternada


print(gerar_lista_alternada(10))
