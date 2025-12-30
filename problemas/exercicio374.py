def agrupar_por_inicial(lista):
    d = {}

    for palavras in lista:
        palavras = palavras.lower()
        primeira_letra = palavras[0]
        if primeira_letra not in d:
            d[primeira_letra] = [palavras]
        else:
            if palavras not in d[primeira_letra]:
                d[primeira_letra].append(palavras)

    return d


lista = ["amor", "amizade", "bondade", "cachorro", "alma", "bituca", "amizade"]
print(agrupar_por_inicial(lista))
