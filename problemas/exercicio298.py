def agrupar_por_tamanho(palavras):
    d = {
        "curtas": [],   # até 3 letras
        "longas": []    # mais de 3 letras
    }

    for palavra in palavras:
        if len(palavra) <= 3:
            d["curtas"].append(palavra)
        else:
            d["longas"].append(palavra)

    return d


palavras = ["sol", "computador", "lua", "python"]
print(agrupar_por_tamanho(palavras))
