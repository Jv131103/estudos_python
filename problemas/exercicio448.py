"""
Faça um programa que:

    Leia três números a, b, c

Faça uma rotação:

    a recebe b

    b recebe c

    c recebe a (valor original)

Mostre o resultado

Dica: use desempacotamento múltiplo.
"""
a = int(input())
b = int(input())
c = int(input())
print(f"{a=}, {b=}, {c=}")

temp = a
a = b
b = c
c = temp
print(f"{a=}, {b=}, {c=}")
