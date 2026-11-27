def cadastrar(estoque, codigo, quantidade):
    if estoque.get(codigo):
        estoque[codigo]["quantidade"] += quantidade
    else:
        estoque[codigo] = {"quantidade": quantidade}

    return estoque


def consultar_quantidade(estoque, codigo):
    if codigo in estoque:
        print("Código", codigo)
        dados = estoque[codigo]
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

        return dados["quantidade"]
    else:
        print("Código não encontrado")
        return 0


estoque = {
    "PRD001": {"quantidade": 15},
    "PRD002": {"quantidade": 7},
    "PRD003": {"quantidade": 20}
}
qtd = consultar_quantidade(estoque, 'PRD001')
print(qtd)

estoque = cadastrar(estoque, 'PRD001', 2)
qtd = consultar_quantidade(estoque, 'PRD001')
print(qtd)

qtd = consultar_quantidade(estoque, 'PRD005')
print(qtd)

estoque = cadastrar(estoque, 'PRD004', 98)
qtd = consultar_quantidade(estoque, 'PRD004')
print(qtd)
