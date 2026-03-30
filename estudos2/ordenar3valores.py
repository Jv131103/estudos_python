def ordenar(n1, n2, n3):
    if n1 > n2:
        n1, n2 = n2, n1

    if n2 > n3:
        n2, n3 = n3, n2

    if n1 > n2:
        n1, n2 = n2, n1

    return n1, n2, n3


def ordenar2(n1, n2, n3):
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    meio = n1 + n2 + n3 - maior - menor

    n1 = menor
    n2 = meio
    n3 = maior

    return n1, n2, n3


def ordenar3(n1, n2, n3):
    lista = [n1, n2, n3]
    lista.sort()
    return tuple(lista)


def ordenar4(n1, n2, n3):
    if n1 <= n2 <= n3:
        return n1, n2, n3
    elif n1 <= n3 <= n2:
        return n1, n3, n2
    elif n2 <= n1 <= n3:
        return n2, n1, n3
    elif n2 <= n3 <= n1:
        return n2, n3, n1
    elif n3 <= n1 <= n2:
        return n3, n1, n2
    else:
        return n3, n2, n1


def ordenar5(n1, n2, n3):
    lista = [n1, n2, n3]

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return tuple(lista)


def ordenar6(n1, n2, n3):
    a = (n1 + n2 + n3 - abs(n1 - n2) - abs(n2 - n3) - abs(n1 - n3)) // 2
    c = (n1 + n2 + n3 + abs(n1 - n2) + abs(n2 - n3) + abs(n1 - n3)) // 2
    b = n1 + n2 + n3 - a - c
    return a, b, c


print(ordenar(1, 2, 3))
print(ordenar(3, 2, 1))
print(ordenar(1, 3, 2))
print(ordenar(2, 3, 1))

print()

print(ordenar2(1, 2, 3))
print(ordenar2(3, 2, 1))
print(ordenar2(1, 3, 2))
print(ordenar2(2, 3, 1))

print()

print(ordenar3(1, 2, 3))
print(ordenar3(3, 2, 1))
print(ordenar3(1, 3, 2))
print(ordenar3(2, 3, 1))

print()

print(ordenar4(1, 2, 3))
print(ordenar4(3, 2, 1))
print(ordenar4(1, 3, 2))
print(ordenar4(2, 3, 1))

print()

print(ordenar5(1, 2, 3))
print(ordenar5(3, 2, 1))
print(ordenar5(1, 3, 2))
print(ordenar5(2, 3, 1))

print()

print(ordenar6(1, 2, 3))
print(ordenar6(3, 2, 1))
print(ordenar6(1, 3, 2))
print(ordenar6(2, 3, 1))
