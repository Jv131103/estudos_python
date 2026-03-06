class RingBuffer:

    def __init__(self, tamanho):
        self.buffer = [None] * tamanho
        self.index = 0
        self.tamanho = tamanho

    def adicionar(self, valor):
        self.buffer[self.index] = valor
        self.index = (self.index + 1) % self.tamanho


r = RingBuffer(5)
r.adicionar("A")
r.adicionar("B")
r.adicionar("C")
r.adicionar("D")
r.adicionar("E")
print(r.buffer)
r.adicionar("F")
r.adicionar("G")
print(r.buffer)
