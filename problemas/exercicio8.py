"""
Faça um programa que receba uma data de nascimento (15/07/87) e
imprima 'Você nasceu em <dia> de <mes> de <ano>'
"""

# Forma 1:
nascimento = input("Sua data de nascimento: ").replace("/", " de ").strip()
print(f"Você nasceu em {nascimento}")

# Forma 2:
nascimento = input("Sua data de nascimento: ").strip().split("/")
dia, mes, ano = nascimento
print(f"Você nasceu em {dia} de {mes} de {ano}")
