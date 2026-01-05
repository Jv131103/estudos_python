def janela_com_soma_exata(lista, alvo):
    inicio = 0
    fim = 0

    soma = 0
    while fim < len(lista):
        soma += lista[fim]

        if soma < alvo:
            fim += 1
        elif soma == alvo:
            return True
        else:
            while soma >= alvo:
                soma -= lista[inicio]
                inicio += 1
    return False


nums = [1, 2, 3, 4]
alvo = 6
print(janela_com_soma_exata(nums, alvo))
