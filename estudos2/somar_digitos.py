def somar_digitos(numero):
    soma = 0
    while numero > 0:
        soma += numero % 10
        numero //= 10

    return soma


print(somar_digitos(1234))
print(somar_digitos(507))
print(somar_digitos(9))
