def janela_com_soma_exata(lista, alvo):
    inicio = 0
    soma = 0

    for fim in range(len(lista)):
        soma += lista[fim]

        while soma > alvo:
            soma -= lista[inicio]
            inicio += 1

        if soma == alvo:
            return True

    return False
