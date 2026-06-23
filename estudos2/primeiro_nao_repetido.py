def encontrar_primeiro_nao_repetido(string):
    if not string:
        raise ValueError("String não pode ser vazio")

    d = {}

    for valor in string:
        d[valor] = d.get(valor, 0) + 1

    for valor in string:
        if d[valor] == 1:
            return valor

    return None


print(encontrar_primeiro_nao_repetido("abacddbec"))
print(encontrar_primeiro_nao_repetido("aabbcc"))
