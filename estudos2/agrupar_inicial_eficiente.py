def agrupar_por_inicial1(lista):
    d = {}

    for palavra in lista:
        palavra = palavra.lower()
        inicial = palavra[0]
        if palavra not in d.setdefault(inicial, []):
            d[inicial].append(palavra)

    return d


def agrupar_por_inicial2(lista):
    d = {}

    for palavra in lista:
        palavra = palavra.lower()
        inicial = palavra[0]
        d.setdefault(inicial, set()).add(palavra)

    return {k: list(v) for k, v in d.items()}


lista = ["amor", "amizade", "bondade", "cachorro", "alma", "bituca", "amizade"]
print(agrupar_por_inicial1(lista))
print(agrupar_por_inicial2(lista))
