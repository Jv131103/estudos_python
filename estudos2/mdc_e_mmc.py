def mdc(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


def mdc2(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def mmc(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // mdc2(a, b)


print(mdc(48, 18))
print(mdc2(48, 18))
print(mdc(-48, 18))
print()
print(mmc(-12, 18))
print(mmc(0, 18))
print(mmc(12, 18))
