class ListaCircular:
    def __init__(self, dados):
        self.dados = dados
        self.n = len(dados)
        self.pos = 0  # posição atual

    def atual(self):
        return self.dados[self.pos]

    def proximo(self):
        self.pos = (self.pos + 1) % self.n
        return self.dados[self.pos]

    def anterior(self):
        self.pos = (self.pos - 1) % self.n
        return self.dados[self.pos]


lc = ListaCircular(["A", "B", "C", "D"])

print(lc.atual())     # A
print(lc.proximo())   # B
print(lc.proximo())   # C
print(lc.proximo())   # D
print(lc.proximo())   # A  ← voltou!
print(lc.anterior())  # D
