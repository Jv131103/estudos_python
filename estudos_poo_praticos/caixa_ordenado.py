class Caixa:
    def __init__(self, valor):
        self.valor = valor
        self.proxima = None  # aponta pra próxima caixa, ou None se for a última


def inserir_ordenado(primeira_caixa, valor):
    nova_caixa = Caixa(valor)

    if primeira_caixa is None:
        return nova_caixa

    if valor < primeira_caixa.valor:
        nova_caixa.proxima = primeira_caixa
        return nova_caixa

    atual = primeira_caixa
    while atual.proxima is not None and atual.proxima.valor < valor:
        atual = atual.proxima

    nova_caixa.proxima = atual.proxima
    atual.proxima = nova_caixa

    return primeira_caixa


c1 = Caixa(10)
c2 = Caixa(20)
c3 = Caixa(30)

c1.proxima = c2
c2.proxima = c3

atual = c1

inserir_ordenado(c1, 15)

while atual:
    print(atual.valor)
    atual = atual.proxima
