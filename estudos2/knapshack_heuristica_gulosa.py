itens = [
    {"nome": "Notebook", "peso": 3, "valor": 4000},
    {"nome": "Celular", "peso": 1, "valor": 2500},
    {"nome": "TV", "peso": 8, "valor": 5000},
    {"nome": "Livro", "peso": 2, "valor": 300},
    {"nome": "Relógio", "peso": 1, "valor": 1200},
]

capacidade = 10

# Heurística: pegar primeiro os itens com maior valor por kg
itens.sort(key=lambda item: item["valor"] / item["peso"], reverse=True)

peso_total = 0
mochila = []

for item in itens:
    if peso_total + item["peso"] <= capacidade:
        mochila.append(item)
        peso_total += item["peso"]

print("Itens escolhidos:")
for item in mochila:
    print(item["nome"])

print("Peso:", peso_total)
print("Valor:", sum(i["valor"] for i in mochila))
