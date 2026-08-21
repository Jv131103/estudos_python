class Caixa:
    def __init__(self, valor):
        self.valor = valor
        self.proxima = None  # aponta pra próxima caixa, ou None se for a última



c1 = Caixa(10)
c2 = Caixa(20)
c3 = Caixa(30)

c1.proxima = c2
c2.proxima = c3

atual = c1

while atual:
    print(atual.valor)
    atual = atual.proxima
