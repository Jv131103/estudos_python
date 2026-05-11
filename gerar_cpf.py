import random


def gerar9digitos():
    valores = []

    for _ in range(9):
        valores.append(random.randint(0, 9))

    return valores


def gerar_digito_verificador1(digitos=[]):
    if not digitos:
        digitos = gerar9digitos()

    peso = 10
    soma = 0

    for valor in digitos:
        valor *= peso
        soma += valor
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto

    digitos.append(digito)
    return digitos


def gerar_digito_verificador2(digitos=[]):
    if not digitos:
        digitos = gerar_digito_verificador1(gerar9digitos())

    peso = 11
    soma = 0

    for valor in digitos:
        valor *= peso
        soma += valor
        peso -= 1

    resto = soma % 11
    if resto < 2:
        digito = 0
    else:
        digito = 11 - resto

    digitos.append(digito)

    return digitos


def gerar_cpf(digitos=[], format=False):
    if not digitos:
        digitos = gerar_digito_verificador2(gerar_digito_verificador1(gerar9digitos()))
    else:
        digitos = gerar_digito_verificador2(gerar_digito_verificador1(digitos))

    if format:
        editado = digitos[:9]
        formatado = []

        contador = 0
        for i in editado:
            if contador % 3 == 0 and contador > 0:
                formatado.append(".")
            formatado.append(i)
            contador += 1

        formatado.append("-")
        formatado.extend(digitos[-2:])

        digitos = formatado

    return "".join(map(str, digitos))


print(gerar_cpf([1, 2, 3, 4, 5, 6, 7, 8, 9], format=True))
print(gerar_cpf([2, 0, 8, 2, 8, 4, 5, 1, 0]))
print(gerar_cpf(format=True))
print(gerar_cpf())
