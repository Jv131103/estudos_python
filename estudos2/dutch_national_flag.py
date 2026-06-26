def dutch_flag(lista):
    baixo = 0
    meio = 0
    alto = len(lista) - 1

    while meio <= alto:
        if lista[meio] == 0:
            # Joga o 0 para a esquerda
            lista[baixo], lista[meio] = lista[meio], lista[baixo]
            baixo += 1
            meio += 1
        elif lista[meio] == 1:
            # O 1 já pertence ao meio, só avança o explorador
            meio += 1
        else:  # lista[meio] == 2
            # Joga o 2 para a direita
            lista[meio], lista[alto] = lista[alto], lista[meio]
            alto -= 1  # Não avançamos o 'meio' aqui porque o elemento que veio de 'alto' ainda precisa ser analisado!

    print(lista)


dutch_flag([2, 0, 2, 1, 1, 0])
