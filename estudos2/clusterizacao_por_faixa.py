produtos = [
    ("Mouse", 80),
    ("Teclado", 150),
    ("Notebook", 4200),
    ("Monitor", 900),
    ("Caneta", 5),
]

clusters = {
    "barato": [],
    "medio": [],
    "caro": []
}

for nome, preco in produtos:

    if preco < 100:
        clusters["barato"].append(nome)

    elif preco < 1000:
        clusters["medio"].append(nome)

    else:
        clusters["caro"].append(nome)

print(clusters)
