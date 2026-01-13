"""
Faça um programa que:

    Leia a idade

    Leia se a pessoa tem autorização (True ou False)

Verifique se pode entrar:

    idade ≥ 18 ou autorização

"""

idade = int(input("Idade: "))
autorizacao = input("Possui autorização? [sim / não] ").lower()

pode_entrar = idade >= 18 or autorizacao == "sim"

print(f"Liberado? {pode_entrar}")
