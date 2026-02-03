"""
Faça dois códigos que:

    Produzam o mesmo resultado

    Um usando walrus

    Outro sem walrus

Depois:

    Compare legibilidade

    Comente qual ficou mais claro e por quê
"""


def com_walrus():
    if (soma := 2 + 2) == 4:
        print(soma)


def sem_walrus():
    soma = 2 + 2
    if soma == 4:
        print(soma)


com_walrus()
sem_walrus()
