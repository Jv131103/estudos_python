def pares_com_soma_dict(lista, alvo):
    vistos = {}
    pares_achados = {}
    resultado = []

    for valor in lista:
        complemento = alvo - valor

        if complemento in vistos:
            menor = valor if valor < complemento else complemento
            maior = complemento if valor < complemento else valor

            par = (menor, maior)

            if par not in pares_achados:
                resultado.append([menor, maior])
                pares_achados[par] = True

        vistos[valor] = True

    return resultado


lista = [2, 7, 11, 15, 3, 6, 4]
alvo = 9
for distintos in pares_com_soma_dict(lista, alvo):
    print(distintos)
