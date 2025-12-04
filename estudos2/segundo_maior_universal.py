def segundo_maior(lista):
    a, b = lista[0], lista[1]

    if a > b:
        maior = a
        segundo = b
    else:
        maior = b
        segundo = a

    for x in lista[2:]:
        if x > maior:
            segundo = maior
            maior = x
        elif segundo < x < maior:
            segundo = x

    return segundo


print(segundo_maior([10, 20, 30, 40]))       # 30
print(segundo_maior([5, 1, 5, 3, 5]))        # 3
print(segundo_maior([-10, -5, -1, -1]))      # -5
