def segundo_maior(lista):
    maior = float("-inf")
    maior_segundo = float("-inf")

    for i in lista:
        if i > maior:
            maior_segundo = maior
            maior = i

        elif maior > i > maior_segundo:
            maior_segundo = i

    return maior_segundo


print(segundo_maior([10, 20, 30, 40]))       # 30
print(segundo_maior([5, 1, 5, 3, 5]))        # 3
print(segundo_maior([-10, -5, -1, -1]))      # -5
