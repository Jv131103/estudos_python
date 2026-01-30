"""
Faça um programa que:

    Crie um gerador que produza números de 1 até n

    Use yield

    Consuma o gerador com um for

Exemplo conceitual:

    n = 5
    Saída: 1 2 3 4 5
"""


def generate_at(n):
    yield from range(1, n + 1)
    return 0


def generate_at2(n):
    for num in range(1, n + 1):
        print(num, end=" ")
        yield num


value = generate_at(5)
for _ in range(5):
    print(next(value), end=" ")
print()


val = generate_at2(5)
for _ in range(5):
    next(val)
print()
