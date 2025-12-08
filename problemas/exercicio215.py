def combinacoes(s):
    resultados = []

    def gerar(prefixo, resto):
        # caso base: não sobrou nada pra decidir
        if not resto:
            resultados.append(prefixo)
            return

        primeira = resto[0]
        resto_faltante = resto[1:]

        # caso 1: incluir a primeira letra
        gerar(prefixo + primeira, resto_faltante)

        # caso 2: NÃO incluir a primeira letra
        gerar(prefixo, resto_faltante)

    gerar("", s)
    return resultados


print(combinacoes("ab"))
print(combinacoes("abc"))
