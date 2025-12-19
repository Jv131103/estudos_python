def agrupar_por_inicial(lista):
    d = {}

    for valor in lista:
        primeiro = valor[0]
        if primeiro not in d:
            d[primeiro] = [valor]
        else:
            d[primeiro].append(valor)

    return d


nomes = ["ana", "alice", "bruno", "bia"]
print(agrupar_por_inicial(nomes))
