def primeiro_digito(numero):
    numero = abs(numero)

    digito = 0
    while numero > 0:
        digito = numero % 10
        numero //= 10

    return digito


def primeiro_digito2(numero):
    numero = abs(numero)

    while numero >= 10:
        numero //= 10

    return numero


print(primeiro_digito(58342))
print(primeiro_digito(0))
print(primeiro_digito(1200))
print(primeiro_digito(-583))
print()
print(primeiro_digito2(58342))
print(primeiro_digito2(0))
print(primeiro_digito2(1200))
print(primeiro_digito2(-583))
