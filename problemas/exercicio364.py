def indice_reverso(frase):
    d = {}

    novo = ""
    for dados in frase:
        if dados not in "!@#$%&*()=-+/%.,;?:><":
            novo += dados

    frase = novo.lower().split()

    for idx, valor in enumerate(frase):
        if valor not in d:
            d[valor] = [idx]
        else:
            d[valor].append(idx)
    return d


valor = "eu gosto de eu estudar"
print(indice_reverso(valor))
