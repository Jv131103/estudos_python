"""
Leia uma string no formato:

    nome,idade

Exemplo:

    Ana,20

Mostre:

    nome

    idade (como inteiro)
"""

informacao = input("Digite no formato [nome,idade]: ").split(",")
if len(informacao) <= 1:
    print("Formatação inválida, precisa estar como: nome,idade")
else:
    nome, idade = informacao

    if not idade.isdigit():
        print("Idade inválida, precisa ser do tipo inteiro")
    else:
        idade = int(idade)

        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
