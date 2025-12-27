class MapaFrequenciaOrdenado:
    def __init__(self):
        self.registro = []   # lista de [valor, frequencia]
        self.historico = []  # ordem de inserção (valores ativos)

    def adicionar(self, valor):
        if valor not in self.historico:
            self.registro.append([valor, 1])
            self.historico.append(valor)
            return

        for item in self.registro:
            if item[0] == valor:
                item[1] += 1
                return

    def remover(self, valor):
        if valor not in self.historico:
            return  # regra: "se não existir, não faz nada"

        for i, item in enumerate(self.registro):
            if item[0] == valor:
                item[1] -= 1

                if item[1] <= 0:
                    self.registro.pop(i)
                    self.historico.remove(valor)
                return

    def itens(self):
        return [(valor, freq) for valor, freq in self.registro]

    def contem(self, valor):
        return valor in self.historico


m = MapaFrequenciaOrdenado()
m.adicionar("a")
m.adicionar("b")
m.adicionar("a")
m.adicionar("c")
m.adicionar("b")
print(m.itens())
