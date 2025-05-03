"""
Faça um programa que receba uma string e reponda se ela têm uma vogal,
se sim quais são? E também diga se é uma frase ou não

PS: Não use laços para essa execução
"""

string = input("Digite um texto: ").lower()

if "a" in string:
    print("Possui a letra a")
if "e" in string:
    print("Possui a letra e")
if "i" in string:
    print("Possui a letra i")
if "o" in string:
    print("Possui a letra o")
if "u" in string:
    print("Possui a letra u")

if " " in string:
    print("É uma frase")
else:
    print("Não é uma frase")
