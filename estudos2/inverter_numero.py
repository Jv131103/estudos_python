def inverter_numero(numero):
    negativo = numero < 0
    numero = abs(numero)

    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    return -invertido if negativo else invertido


print(inverter_numero(58342))
print(inverter_numero(0))
print(inverter_numero(1200))
print(inverter_numero(-583))
