def maior_e_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for valor in lista:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    return maior, menor


def soma_lista(lista):
    soma = 0
    for valor in lista:
        soma += valor

    return soma


def quantidade_elementos(lista):
    qtd = 0
    for _ in lista:
        qtd += 1
    return qtd


def media_lista(lista):
    return soma_lista(lista) / quantidade_elementos(lista)


def moda_lista(lista):
    frequencias = {}
    for valor in lista:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1

    maior_freq = 0
    for qtd in frequencias.values():
        if qtd > maior_freq:
            maior_freq = qtd

    resultado = []
    for valor, qtd in frequencias.items():
        if qtd == maior_freq:
            resultado.append(valor)

    return resultado


def mediana_lista(lista):
    # 1) Ordenar a lista manualmente
    lista_ordenada = sorted(lista)

    n = quantidade_elementos(lista_ordenada)
    meio = n // 2

    # 2) Se quantidade for ímpar → pega o elemento central
    if n % 2 != 0:
        return lista_ordenada[meio]

    # 3) Se quantidade for par → média dos dois centrais
    else:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2


def variancia_lista(lista):
    # 1) Calcula a média
    media = media_lista(lista)

    # 2) Soma dos quadrados das diferenças
    soma_quadrados = 0
    for v in lista:
        soma_quadrados += (v - media) ** 2

    # 3) Variância populacional
    return soma_quadrados / quantidade_elementos(lista)


def desvio_padrao_lista(lista):
    var = variancia_lista(lista)
    # raiz quadrada sem biblioteca:
    desvio = var ** 0.5
    return desvio


lista = [
    -1505, 2518, 2333, 4682, -1740, 1067, 995, 22,
    -1153, -4098, 4560, 2958, 3640, -4154, 2345, 4,
    -1601, 158, -4044, -98, 707, 359, -3088, 527,
    -3004, -4045, 563, -4137, 4598, -3862, 488, -1,
    3445, 3820, 504, -1475, 1626, -1252, 2059, 16,
    -1472, 2610, -4643, 2912, -2517, -4604, -1476,
    3950, -4640, -229, 229, -3452, 4309, 2356, 66,
    3728, -1846, -635, -3581, 4457, -2592, -1066,
    -1006, -164, 805, -4500, -455, 2245, -4959,
    -2415, 2038, 4512, 1243, 349, -1153, 3623, 631,
    2209, -3349, -2417, 4429, -1324, -4101, -1354,
    4400, -4968, -4433, 2042, 904, 932, 1331, 4955,
    -3775, -333, 1012, 2192, -161, -224, 1505, -1615,
    -2165, 3666, -4253, -358, -3939, -2641, 1228,
    -608, -2280, 4939, -3355, 1340, -57, 3346, 2686,
    -1572, 1991, -2351, -3972, -1683, -1509, -2488,
    266, -2991, -795, -4032, 2397, 2391, 3654, -1044,
    -2204, -2440, -1280, 2714, -4151, -1951, 3684,
    -4251, 3748, -4359, -1436, -2190, 4538, -3563,
    1542, 1926, -3940, -2274, -4223, 2504, -4112, 2388,
]

maior, menor = maior_e_menor(lista)
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")
soma = soma_lista(lista)
print(f"Soma de todos os elementos da lista {soma}")
tam = quantidade_elementos(lista)
print(f"Quantidade de elementos da lista: {tam}")
media = media_lista(lista)
print(f"Média aritmética: {media:.2f}")
moda = moda_lista(lista)
print(f"Moda: {moda}")
mediana = mediana_lista(lista)
print(f"Mediana: {mediana}")
variancia = variancia_lista(lista)
print(f"Variância: {variancia:.3f}")
desvio = desvio_padrao_lista(lista)
print(f"Desvio padrão: {desvio:.3f}")
