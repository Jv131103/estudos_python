"""
Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.


Dica: utilize o módulo math do Python, especificamente math.fatorial.
"""

n = int(input("fatorial de: "))

# modelo 1:
mult = 1
for i in range(n, 1, -1):
    mult *= i
print(mult)

# modelo 2:
import math

print(math.factorial(n))
