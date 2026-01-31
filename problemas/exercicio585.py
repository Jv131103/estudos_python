"""
Faça um programa que:

    Leia um valor do usuário

    Tente converter para inteiro

    Trate apenas o erro correto

    Em caso de erro, mostre uma mensagem amigável
"""

try:
    num = int(input("Número inteiro: "))
except ValueError:
    print("NÚMERO PRECISA SER DO TIPO INTEIRO")
