"""
Faça um programa que itera em uma string e toda vez que uma vogal aparecer
na sua string, print o seu nome entre as letras
"""


# Versão 1
string = input("Digite uma string: ").strip().lower()

for letra in string:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        print("João")
    else:
        print(letra)


# versão 2
string = input("Digite uma string: ").strip().lower()
vogais = "aeiou"

for letra in string:
    if letra in vogais:
        print("João")
    else:
        print(letra)
