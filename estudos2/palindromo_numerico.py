def eh_palindromo_numerico(numero):
    original = numero

    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    return invertido == original


print(eh_palindromo_numerico(121))
print(eh_palindromo_numerico(1331))
print(eh_palindromo_numerico(123))
print(eh_palindromo_numerico(-121))
