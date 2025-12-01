def retornar_decimal(binario):
    binario = str(binario)

    tamanho = len(binario) - 1

    soma_decimal = 0
    indice = 0
    for potencia in range(tamanho, -1, -1):
        soma_decimal += int(binario[indice]) * 2**potencia
        indice += 1
    return soma_decimal


def retornar_binario(numero):
    lista_restos = []
    while numero != 0:
        numero, resto = numero // 2, numero % 2
        lista_restos.append(resto)

    resultado = ""
    for i in range(len(lista_restos) - 1, -1, -1):
        resultado += str(lista_restos[i])
    return resultado


print(retornar_binario(13))   # "1101"
print(retornar_decimal("1101"))  # 13
print(retornar_decimal("10000"))  # 16
