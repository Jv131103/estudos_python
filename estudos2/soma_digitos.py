def soma_digitos(numero):
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise ValueError("Número só pode ser do tipo int")
    elif numero < 0:
        numero = abs(numero)

    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10

    return soma


print(soma_digitos(12345))
print(soma_digitos(48))
