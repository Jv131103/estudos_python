def inverter_dict(dicionario):
    if not dicionario:
        return {}

    inverso = {}
    for chave, valor in dicionario.items():
        if valor in inverso:
            raise ValueError(f"Valor duplicado encontrado: '{valor}' já está associado a '{inverso[valor]}'")
        inverso[valor] = chave

    return inverso


def inverter_dict2(dicionario):
    if not dicionario:
        return {}

    itens = list(dicionario.items())  # congela os itens ANTES de mexer no dict
    dicionario.clear()                # esvazia o dicionário original

    for chave, valor in itens:
        dicionario[valor] = chave

    return dicionario


capitais = {"Brasil": "Brasília", "França": "Paris", "Japão": "Tóquio"}
print(inverter_dict(capitais))
print(inverter_dict2(capitais))
