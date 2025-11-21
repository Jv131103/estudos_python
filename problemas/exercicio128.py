def media(lista_notas):
    return sum(lista_notas) / len(lista_notas)


def media2(lista_notas):
    soma = 0
    total_notas = 0

    for i in lista_notas:
        soma += i
        total_notas += 1

    return soma / total_notas


lista_notas = [5, 5, 5, 5, 5]
print(media(lista_notas))
print(media2(lista_notas))
