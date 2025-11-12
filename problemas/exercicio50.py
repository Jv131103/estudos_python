"""
Escreva um programa que mostre de 50 até 1 na tela.
"""

# Modelo 1
cont = 50
while cont >= 1:
    print(cont)
    cont -= 1


# Modelo 2
for i in range(50, 0, -1):
    print(i)
