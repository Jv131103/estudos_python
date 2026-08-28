class Bifurcacao:
    def __init__(self, valor):
        self.valor = valor
        self.caminho_par = None    # pra onde ir se o próximo número for par
        self.caminho_impar = None  # pra onde ir se for ímpar


b1 = Bifurcacao(100)
b2 = Bifurcacao(200)
b3 = Bifurcacao(300)
b4 = Bifurcacao(400)

b1.caminho_par = b2
b1.caminho_impar = b3

b2.caminho_par = b4
b2.caminho_impar = b4  # pode reaproveitar o mesmo destino, sem problema

atual = b1
lista = [4, 7, 2]

for numero in lista:
    print(f"Número {numero}, estou no nó de valor {atual.valor}")
    if numero % 2 == 0:
        atual = atual.caminho_par
    else:
        atual = atual.caminho_impar
