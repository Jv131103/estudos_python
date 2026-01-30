"""
Faça um programa que:

    Crie dois geradores:

        um que gere números de 0 a 2

        outro que gere números de 3 a 5

    Crie um terceiro gerador que una os dois usando yield from

    Consuma o gerador final

Exemplo conceitual:

    Saída: 0 1 2 3 4 5
"""


def gen1():
    yield from range(3)


def gen2():
    yield from range(3, 6)


def gen3():
    yield from gen1()
    yield from gen2()


valores = gen3()
for _ in range(6):
    print(next(valores), end=" ")
print()
