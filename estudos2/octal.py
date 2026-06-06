def dec_to_oct(numero):
    lista = []
    while numero > 0:
        lista.append(str(numero % 8))
        numero //= 8
    lista.append("o")
    lista.append("0")

    return "".join(reversed(lista))


def oct_to_dec(numero):
    if "0o" in numero:
        numero = numero.replace("0o", "")

    tam_posicao = len(numero) - 1

    soma = 0
    for dado in numero:
        calculo = int(dado) * 8**tam_posicao

        soma += calculo
        tam_posicao -= 1

    return soma


valor = dec_to_oct(92)
print(valor)
final = oct_to_dec(valor)
print(final)
