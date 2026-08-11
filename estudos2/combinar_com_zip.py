produtos = ["Notebook", "Mouse", "Teclado", "Monitor"]
precos = [3500.00, 89.90, 150.00, 1200.00]

if len(produtos) != len(precos):
    raise ValueError("Tamanhos da lista não batem entre si")

lista = []

mais_caro = 0
item = ""
for produto, preco in zip(produtos, precos):
    item_dict = {"produto": produto, "precos": preco}
    lista.append(item_dict)
    if preco > mais_caro:
        item = produto
        mais_caro = preco


print("Objeto final:", lista)
print(f"Valor mais caro: {item} | Preço: {mais_caro:.2f}")
print(f"Total: {sum(precos):.2f}")
