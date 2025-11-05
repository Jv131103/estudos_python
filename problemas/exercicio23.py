"""
Faça um programa que calcule a raiz quadrada de um número. O usuário deve
inserir um número e o programa deve mostrar na tela o resultado da raiz
quadrada do número inserido.
"""

n1 = int(input("Digite um número: "))

# Método 1:
import math

print(math.sqrt(n1))

# Método 2:
print(n1**(1 / 2))

# Método 3:
print(pow(n1, 0.5))  # n1 ** 0.5

# Método 4: Esse método é usado em calculadoras e hardware.
n = n1
x = n / 2  # chute inicial
for _ in range(10):  # itera 10 vezes
    x = (x + n / x) / 2
print(x)

# Método 5: Só funciona para quadrados perfeitos (ex.: 9, 16, 25)
n = n1
count = 0
impar = 1
while n > 0:
    n -= impar
    impar += 2
    count += 1
print(count)
