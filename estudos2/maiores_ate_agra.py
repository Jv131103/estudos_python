def maiores_ate_agora(lista):
    if not lista:
        return []

    resultado = [0] * len(lista)

    maior = lista[0]

    i = 0
    for valor in lista:
        if valor > maior:
            maior = valor

        resultado[i] = maior
        i += 1

    return resultado


lista = [3, 1, 5, 2, 7]

print(maiores_ate_agora(lista))
