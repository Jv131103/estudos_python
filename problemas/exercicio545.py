"""
Faça um programa que:

    Leia nome, idade e cidade

    Armazene esses dados em uma tupla

    Desempacote a tupla em variáveis separadas

    Mostre os valores na tela

Exemplo conceitual:

    Tupla: ("Ana", 20, "SP")

DICAS

    Use empacotamento automático

    Use desempacotamento direto (a, b, c = tupla)

    Lembre: tupla representa um “registro simples”
"""

tupla = input("Nome: "), int(input("Idade: ")), input("cidade: ")
print(tupla)

nome, idade, cidade = tupla

print(nome, idade, cidade)
