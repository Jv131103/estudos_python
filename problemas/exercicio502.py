"""
Faça uma função recursiva que:

    Receba n

    Retorne a soma 1 + 2 + ... + n

Não use loop.
"""


def soma(n):
    if n == 0:
        return n
    return n + soma(n - 1)


print(soma(3))
print(soma(5))
