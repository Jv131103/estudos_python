"""
Faça um programa que:

    Leia dois valores do usuário

    Primeiro:

        trate erro de conversão

    Depois:

        trate erro de divisão por zero

    Use try/except aninhados
"""

try:
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    try:
        divisao = n1 / n2
        print(divisao)
    except ZeroDivisionError:
        print("Erro de divisão por 0")
except ValueError:
    print("Dados precisam ser numéricos")
