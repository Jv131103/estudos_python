"""
Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar. A mensagem na tela deverá seguir o seguinte formato:

"O número [número] é [par/ímpar]"
"""


def par1(number):
    return number % 2 == 0


def par2(number):
    return number & 1 == 0


def par3(number):
    return (number // 2) * 2 == number


number = int(input("DIGITE UM NÚMERO: "))
if par1(number) and par2(number) and par3(number):
    print("É PAR")
else:
    print("É ÍMPAR")
