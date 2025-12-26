def processar1(lista):
    soma = 0
    for x in lista:
        if x > 0:
            soma += x
    return soma


def processar2(lista):
    return sum(i for i in lista if i > 0)


def exibir(func, dados):
    print("++" * 30)
    print(f"Resultado: {func(dados)}")
    print("++" * 30)


dados = [-2, -1, 0, 1, 2]
testes = processar1, processar2
for testar in testes:
    exibir(testar, dados)
