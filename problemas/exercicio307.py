def top_frequencia(lista):
    d = {}

    for letra in lista:
        d[letra] = d.get(letra, 0) + 1

    maior = 0
    for chave, valor in d.items():
        if valor > maior:
            maior = valor
            item = chave

    return item


print(top_frequencia(["a", "b", "a", "c", "b", "a"]))
