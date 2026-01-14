"""
Faça um programa que:

    . Leia a idade

Verifique se a pessoa está na faixa:

. entre 18 e 65 anos (inclusive)

Mostre True ou False
"""
idade = int(input("Idade? "))
print(f"Está na faixa [18, 65]? {idade >= 18 and idade <= 65}")
