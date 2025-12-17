def pares_maiores_que_10(lista):
    soma = 0
    for numeros in lista:
        if numeros & 1 == 0 and numeros > 10:
            soma += numeros

    return soma


lista = [2, 10, 12, 15, 20]
print(pares_maiores_que_10(lista))
