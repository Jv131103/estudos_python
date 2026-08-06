def maior_valor(lista):
    maior = lista[0]

    for valor in lista[1:]:
        if valor > maior:
            maior = valor

    return maior


def menor_valor(lista):
    menor = lista[0]

    for valor in lista[1:]:
        if valor < menor:
            menor = valor

    return menor


def media(lista):
    soma = 0
    qtd = 0

    for valor in lista:
        soma += valor
        qtd += 1

    return round(soma / qtd, 1)


def estatistica(lista):
    if not isinstance(lista, list):
        raise TypeError("Parâmetro lista precisa ser do tipo 'list'")
    elif not lista:
        raise ValueError("Lista não pode ser vazio...")

    maior = maior_valor(lista)
    menor = menor_valor(lista)
    med = media(lista)

    return maior, menor, med  # retorna uma tupla


# quem chama decide se quer imprimir ou usar os valores
maior, menor, med = estatistica([4, 8, 15, 16, 23, 42])
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Média: {med}")
