def dec_to_hex(numero):
    letras = {
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }

    lista = []
    while numero > 0:
        valor = numero % 16
        if letras.get(valor):
            lista.append(letras[valor])
        else:
            lista.append(str(valor))
        numero //= 16

    lista.append("x")
    lista.append("0")

    return "".join(reversed(lista))


def hex_to_dec(numero):
    if "0x" in numero:
        numero = numero.replace("0x", "")

    tam_posicao = len(numero) - 1

    letras = {
        'a': 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
    }

    soma = 0
    for dado in numero:
        if letras.get(dado):
            calculo = letras[dado] * 16**tam_posicao
        else:
            calculo = int(dado) * 16**tam_posicao

        soma += calculo
        tam_posicao -= 1

    return soma
