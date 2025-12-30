def acima_da_media(valores):

    if not valores:
        return None

    soma = 0
    for v in valores:
        soma += v

    media = soma / len(valores)

    cont = 0
    numeros = []
    for v in valores:
        if v > media:
            numeros.append(v)
            cont += 1

    return {
        "media": media,
        "numeros_acima_da_media": numeros,
        "total_acima_da_media": cont
    }


print(acima_da_media([10, 20, 30, 40]))
