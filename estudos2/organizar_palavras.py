def organizar_palavras(palavras):
    resultado = {
        "curtas": [],
        "longas": [],
        "total_letras": 0
    }

    for palavra in palavras:
        if len(palavra) <= 4:
            resultado["curtas"].append(palavra)
        else:
            resultado["longas"].append(palavra)

        resultado["total_letras"] += len(palavra)

    return resultado


print(organizar_palavras(["casa", "python", "sol", "programar"]))
print(organizar_palavras(["oi", "uva", "lua"]))
print(organizar_palavras(["banana", "computador"]))
print(organizar_palavras(["amor", "livro"]))
print(organizar_palavras([]))
print(organizar_palavras(["", "teste", "a"]))
