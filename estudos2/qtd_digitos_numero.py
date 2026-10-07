def qtd_digitos(numero):
    if type(numero) is not int:
        raise TypeError(
            f"'numero' deve ser int, não {type(numero).__name__}"
        )

    if numero < 0:
        numero = abs(numero)
    elif numero == 0:
        return 1

    cont = 0

    while numero > 0:
        numero //= 10
        cont += 1

    return cont


print(qtd_digitos(58342))
print(qtd_digitos(0))
print(qtd_digitos(9))
print(qtd_digitos(24))
print(qtd_digitos(-583))
