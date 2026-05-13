import random


def gerar12digitos():
    valores = []

    for _ in range(12):
        valores.append(random.randint(0, 9))

    return valores


def gerar_digito_verificador1(digitos=[]):
    if not digitos:
        digitos = gerar12digitos()

    peso = 5
    soma = 0

    for valor in digitos:
        valor *= peso
        soma += valor
        if peso <= 2:
            peso = 9
        else:
            peso -= 1

    resto = soma % 11

    if resto < 2:
        digito = 0
    elif resto >= 2:
        digito = 11 - resto

    digitos.append(digito)
    return digitos


def gerar_digito_verificador2(digitos=[]):
    if not digitos:
        digitos = gerar_digito_verificador1(gerar12digitos())
    elif len(digitos) < 13:
        digitos = gerar_digito_verificador1(digitos)

    peso = 6
    soma = 0

    for valor in digitos:
        valor *= peso
        soma += valor
        if peso <= 2:
            peso = 9
        else:
            peso -= 1

    resto = soma % 11

    if resto < 2:
        digito = 0
    elif resto >= 2:
        digito = 11 - resto

    digitos.append(digito)
    return digitos


def gerar_cnpj(digitos=[], format=False):
    if not digitos:
        digitos = gerar_digito_verificador2(gerar_digito_verificador1(gerar12digitos()))
    else:
        digitos = gerar_digito_verificador2(gerar_digito_verificador1(digitos))

    if format:
        formatado = digitos[:2]
        formatado.append(".")

        editado = digitos[2:8]
        contador = 0
        for i in editado:
            if contador % 3 == 0 and contador > 0:
                formatado.append(".")
            formatado.append(i)
            contador += 1
        formatado.append("/")

        editado = digitos[8:12]
        formatado.extend(editado)
        formatado.append("-")
        formatado.extend(digitos[12:])

        digitos = formatado

    return "".join(map(str, digitos))


print(gerar_cnpj([1, 7, 8, 7, 8, 5, 8, 1, 0, 0, 0, 1]))
print(gerar_cnpj([1, 7, 8, 7, 8, 5, 8, 1, 0, 0, 0, 1], format=True))
print(gerar_cnpj())
print(gerar_cnpj(format=True))
