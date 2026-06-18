def inverter(numero):
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise ValueError("numero, precisa ser do tipo inteiro")

    eh_negativo = False
    if numero < 0:
        numero = abs(numero)
        eh_negativo = True

    invertido = 0
    while numero != 0:
        dresto = numero % 10
        invertido = (invertido * 10) + dresto
        numero //= 10

    return invertido if not eh_negativo else -invertido


if __name__ == "__main__":
    print(inverter(12345))
    print(inverter(-9001))
    print(inverter(True))
