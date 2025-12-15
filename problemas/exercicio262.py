def maior_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c


def maior_de_tres2(a, b, c):
    return max(a, b, c)


print(maior_de_tres(1, 2, 3))
print(maior_de_tres(3, 2, 1))
print(maior_de_tres(2, 3, 1))
print()
print(maior_de_tres2(1, 2, 3))
print(maior_de_tres2(3, 2, 1))
print(maior_de_tres2(2, 3, 1))
