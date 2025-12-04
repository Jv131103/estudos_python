def primeira_unica(texto):
    # Remover pontuação
    for p in ",.;!?":
        texto = texto.replace(p, "")

    palavras = texto.lower().split()

    # 1) Contar
    contagem = {}
    for p in palavras:
        contagem[p] = contagem.get(p, 0) + 1

    # 2) Achar a primeira que aparece apenas 1 vez
    for p in palavras:
        if contagem[p] == 1:
            return p

    return None  # caso nenhuma palavra seja única


print(primeira_unica("o rato roeu a roupa do rei de roma"))
print(primeira_unica("a a bola bola casa casa unica teste teste"))
