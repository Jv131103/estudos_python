def realizar_contagem_sequencial(casas):
    inicio = [0] * casas

    while True:
        print(inicio)

        i = casas - 1

        while i >= 0:
            if inicio[i] < 9:
                inicio[i] += 1
                break

            inicio[i] = 0
            i -= 1

        if i < 0:
            break


realizar_contagem_sequencial(3)
