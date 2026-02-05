def generate_bin(number):
    retorno = []
    while number > 0:
        retorno.append(number % 2)
        number //= 2

    resultado = "".join(map(str, retorno))

    final = ""
    for valor in range(len(resultado) - 1, -1, -1):
        final += resultado[valor]

    return final


def generate_decimal(binary):
    tamanho = 0
    bin_novo = binary
    while binary > 0:
        tamanho += 1
        binary //= 10

    pot = 0
    soma = 0
    while pot < tamanho:
        soma += 2**pot * (bin_novo % 10)
        bin_novo //= 10
        pot += 1

    return soma


print(generate_bin(100))
print(generate_decimal(1100100))
