"""
Escreva um programa que peça um número inteiro do usuário e mostre na tela o
fatorial deste número.
"""

# versão 1
n = int(input("N: "))
mult = 1
while n > 0:
    mult *= n
    n -= 1
print(mult)

print()

# versão 2
n = int(input("N: "))
mult = 1
for i in range(n, 0, -1):
    mult *= i
print(mult)
