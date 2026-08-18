def soma(numero):
    if numero == 0:
        return 0

    return numero % 10 + soma(numero // 10)


def raiz_digital(numero):
    while numero > 9:
        numero = soma(numero)

    return numero


print(raiz_digital(9875))
