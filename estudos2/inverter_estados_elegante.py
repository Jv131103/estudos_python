def inverter_a_seus_estados(dados):
    final = {}

    for nome, estado in dados.items():
        final[estado] = final.get(estado, []) + [nome]

    return final


def inverter_a_seus_estados2(dados):
    final = {}

    for nome, estado in dados.items():
        final.setdefault(estado, []).append(nome)

    return final


dados = {"ana": "SP", "joao": "RJ", "bia": "SP", "cai": "MG"}
print(inverter_a_seus_estados(dados))
print(inverter_a_seus_estados2(dados))
