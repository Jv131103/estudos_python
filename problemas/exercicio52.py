"""
Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.
"""


# primeiros 20
cont = 0

while cont <= 20:
    if cont % 5 == 0:
        print(cont)
    cont += 1

print()

# 20 primeiros
cont = 0
x = 1

while cont <= 20:
    if x % 5 == 0:
        print(x)
        cont += 1
    x += 1
