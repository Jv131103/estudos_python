"""
Escreva um programa que peça o nome e a idade do usuário. Caso a idade do
usuário seja maior ou igual a 18 anos apresente a seguinte mensagem:
"Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte
mensagem: "Você não pode acessar nosso site [nome].".
"""

nome = input("SEU NOME: ").strip().title()
idade = int(input(f"SUA IDADE {nome}: "))
if idade >= 18:
    print(f"Seja bem-vindo ao nosso site {nome}")
else:
    print(f"você não pode acessar o nosso site {nome}")
