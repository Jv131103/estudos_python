produtos = [
    {"nome": "teclado", "preco": 150},
    {"nome": "mouse", "preco": 80},
    {"nome": "monitor", "preco": 900},
    {"nome": "headset", "preco": 120},
    {"nome": "mousepad", "preco": 40},
]

# Aplicar 10% de desconto
desconto = map(
    lambda p: {
        "nome": p["nome"],
        "preco": p["preco"] * 0.9
    },
    produtos
)

# Filtrar quem continua acima de R$80
filtrados = filter(
    lambda p: p["preco"] > 80,
    desconto
)

# Retornar apenas os nomes em maiúsculo
resultado = list(
    map(
        lambda p: p["nome"].upper(),
        filtrados
    )
)

print(resultado)
