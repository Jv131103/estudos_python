class HistoricoNumerico:
    def __init__(self) -> None:
        self.numeros = []

    def adicionar(self, numero):
        if not isinstance(numero, (int, float)):
            raise TypeError("Número inválido")
        self.numeros.append(numero)

    def is_empty(self):
        return len(self.numeros) == 0

    def media(self, casas_decimais=2):
        if self.is_empty():
            return None
        return round(sum(self.numeros) / len(self.numeros), casas_decimais)

    def maior(self):
        if self.is_empty():
            return None
        return max(self.numeros)

    def menor(self):
        if self.is_empty():
            return None
        return min(self.numeros)


hn = HistoricoNumerico()
hn.adicionar(1)
hn.adicionar(2)
hn.adicionar(3)
hn.adicionar(4)
hn.adicionar(5)
print(hn.media(2))
print(hn.menor())
print(hn.maior())
