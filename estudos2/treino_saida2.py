x = 10


def func():
    # Resolução do bug
    global x
    x = x + 5
    return x


print(func())
