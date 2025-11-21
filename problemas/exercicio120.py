produtos = {
    'geladeira': 1619.1,
    'ps5': 4999,
    'liquidificador': 89.9,
    'notebook': 3500,
    'TV': 1500,
    'ventilador': 79.99,
    'microondas': 399.99
}

selecao = {chave: valor for chave, valor in produtos.items() if valor > 2000}

soma = sum(produtos.values())
print(selecao, soma)
