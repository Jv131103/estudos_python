"""
Faça uma função recursiva que:

    Calcule n!

    Trate 0! = 1
"""


def fatorial(n):
    if n == 0:
        return 1

    if n == 1:
        return n

    return n * fatorial(n - 1)


print(fatorial(0))
print(fatorial(1))
print(fatorial(3))
print(fatorial(5))
