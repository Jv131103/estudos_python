def decimal_para_binario_decimal(numero):
    lista = []

    while numero > 0:
        lista.append(str(numero % 2))
        numero //= 2

    if not lista:
        return "0"

    lista.reverse()
    return "".join(lista)


def decimal_para_binario_bitwise(numero):
    if numero == 0:
        return "0"

    lista = []

    while numero > 0:
        lista.append(str(numero & 1))
        numero >>= 1

    lista.reverse()
    return "".join(lista)


print(decimal_para_binario_decimal(10))
print(decimal_para_binario_bitwise(10))
print(decimal_para_binario_decimal(7))
print(decimal_para_binario_bitwise(7))
print(decimal_para_binario_decimal(25))
print(decimal_para_binario_bitwise(25))
print(decimal_para_binario_decimal(0))
print(decimal_para_binario_bitwise(0))
print(decimal_para_binario_decimal(1))
print(decimal_para_binario_bitwise(1))
