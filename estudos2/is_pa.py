def eh_pa(linha):
    if len(linha) < 2:
        return True

    diff = linha[1] - linha[0]

    for i in range(2, len(linha)):
        if linha[i] - linha[i - 1] != diff:
            return False

    return True


def soma_pa_segura(linha):

    if not eh_pa(linha):
        raise ValueError("linha não é progressão aritmética")

    n = len(linha)
    return n * (linha[0] + linha[-1]) // 2


matriz = [
    [1, 2, 3],   # PA
    # [4, 7, 9],   # NÃO é PA
]
for linha in matriz:
    print(soma_pa_segura(linha))
