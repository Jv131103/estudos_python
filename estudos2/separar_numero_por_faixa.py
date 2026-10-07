def separar_numeros(lista):
    positivos = []
    zeros = []
    negativos = []

    for valor in lista:
        if valor > 0:
            positivos.append(valor)
        elif valor < 0:
            negativos.append(valor)
        else:
            zeros.append(valor)

    return positivos, negativos, zeros


def qtd_valores(lista):
    return len(lista)


def maior_positivo(lista):
    if not lista:
        return None

    maior = lista[0]

    for valor in lista[1:]:
        if valor > maior:
            maior = valor

    return maior


def menor_negativo(lista):
    if not lista:
        return None

    menor = lista[0]

    for valor in lista[1:]:
        if valor < menor:
            menor = valor

    return menor


lista = [5, -2, 0, 8, -7, 0, 3, -1]
positivos, negativos, zeros = separar_numeros(lista)
print(f"Negativos: {negativos}")
print(f"Quantidade de negativos: {qtd_valores(negativos)}")
print(f"Zeros: {zeros}")
print(f"Quantidade de zeros: {qtd_valores(zeros)}")
print(f"Positivos: {positivos}")
print(f"Quantidade de positivos: {qtd_valores(positivos)}")
print()
print(f"Maior positivo: {maior_positivo(positivos)}")
print(f"Menor negativo: {menor_negativo(positivos)}")
