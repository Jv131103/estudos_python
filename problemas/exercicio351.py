def executar(frase, sort=False):
    itens = frase.split()

    d = {}

    for valores in itens:
        tam = len(valores)
        if tam not in d:
            d[tam] = [valores]
        else:
            if valores not in d[tam]:
                d[tam].append(valores)

    if sort:
        editado = {}
        ordens = sorted(d)
        for ordem in ordens:
            editado[ordem] = d[ordem]

        return editado

    return d


print(executar("Python é uma linguagem muito poderosa"))
