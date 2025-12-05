def contar_letras(texto):
    for p in ",.;!?":
        texto = texto.replace(p, "")

    palavras = texto.lower().replace(" ", "")

    contagem = {}
    for p in palavras:
        contagem[p] = contagem.get(p, 0) + 1

    return contagem


print(contar_letras("banana"))
