"""
Faça um programa que:

    . Crie um dicionário com dados de um usuário:

        nome, idade, cidade

    . Use:

        get para acessar uma chave existente

        get para acessar uma chave inexistente com valor padrão

    . Mostre os resultados
"""

usuario = {
    "nome": "João",
    "idade": 22,
    "cidade": "SP"
}

# chave existente
nome = usuario.get("nome")
print("Nome:", nome)

# chave inexistente com valor padrão
email = usuario.get("email", "Não informado")
print("Email:", email)
