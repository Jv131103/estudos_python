class Bolsa:
    def __init__(self) -> None:
        self.multiset = []

    def adicionar(self, valor):
        self.multiset.append(valor)

    def remover(self, valor):
        if valor in self.multiset:
            self.multiset.pop(self.multiset.index(valor))

    def contar(self, valor):
        cont = 0
        for dado in self.multiset:
            if valor == dado:
                cont += 1
        return cont

    def itens(self):
        ja_foi = []
        dados = []
        for dado in self.multiset:
            if dado not in ja_foi:
                dados.append((dado, self.contar(dado)))
                ja_foi.append(dado)
        return dados


bolsa_da_jurumela = Bolsa()
bolsa_da_jurumela.adicionar("Bolsinha")
bolsa_da_jurumela.adicionar("Bolsinha")
bolsa_da_jurumela.adicionar("Bolsinha")
bolsa_da_jurumela.adicionar("Cartas")
bolsa_da_jurumela.adicionar("Maquiagem")
bolsa_da_jurumela.adicionar("Celular")
bolsa_da_jurumela.adicionar("Luvas")
bolsa_da_jurumela.adicionar("Luvas")
bolsa_da_jurumela.adicionar("Dinheiro")
print(bolsa_da_jurumela.contar("Bolsinha"))
bolsa_da_jurumela.remover("Bolsinha")
print(bolsa_da_jurumela.contar("Bolsinha"))
print(bolsa_da_jurumela.itens())
