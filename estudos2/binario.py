def dec_to_bin(numero):
    lista = []
    while numero > 0:
        lista.append(str(numero % 2))
        numero //= 2
    lista.append("b")
    lista.append("0")

    return "".join(reversed(lista))


def bin_to_dec(numero):
    if "0b" in numero:
        numero = numero.replace("0b", "")

    tam_posicao = len(numero) - 1

    soma = 0
    for dado in numero:
        calculo = int(dado) * 2**tam_posicao

        soma += calculo
        tam_posicao -= 1

    return soma
