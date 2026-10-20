def resumir_vendas(vendas):
    status_final = {}

    for categoria, valor in vendas:
        if categoria in status_final:
            status_final[categoria]["total"] += valor
            status_final[categoria]["quantidade"] += 1
        else:
            objeto = {"total": valor, "quantidade": 1}
            status_final[categoria] = objeto

    return status_final


vendas = [
    ("livros", 30),
    ("jogos", 50),
    ("livros", 20),
    ("papelaria", 10),
    ("jogos", 25)
]
print(resumir_vendas(vendas))
