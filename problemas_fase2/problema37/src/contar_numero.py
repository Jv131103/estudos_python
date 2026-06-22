def contar_numero(numero):
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise ValueError("Número, precisa ser do tipo inteiro")
    elif numero == 0:
        return 1
    elif numero < 0:
        numero = abs(numero)

    cont = 0
    while numero > 0:
        cont += 1
        numero //= 10

    return cont


if __name__ == "__main__":
    print(contar_numero(12345))
    print(contar_numero(9))
    print(contar_numero(1000000))
