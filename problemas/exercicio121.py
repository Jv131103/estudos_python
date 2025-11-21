def soma(x, y):
    return x + y


def soma_recursiva(n):
    if n == 0:
        return n
    return n + soma_recursiva(n - 1)


print(soma(1, 5))
print(soma_recursiva(5))
