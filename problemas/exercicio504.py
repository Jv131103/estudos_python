"""
Faça uma função recursiva que:

    Calcule a^b

    Sem usar ** nem pow

Caso base: b == 0
"""


def pot(a, b):
    if b == 0:
        return 1

    return a * pot(a, b - 1)


print(pot(2, 0))
print(pot(2, 1))
print(pot(2, 2))
print(pot(2, 3))
print(pot(2, 4))
print(pot(2, 5))
print(pot(2, 6))
