def inverter_a_seus_estados(dados):
    final = {}
    for valor in dados.values():
        final[valor] = []

    for chave, valor in dados.items():
        final[valor].append(chave)

    print(final)


dados = {"ana": "SP", "joao": "RJ", "bia": "SP", "cai": "MG"}
inverter_a_seus_estados(dados)
