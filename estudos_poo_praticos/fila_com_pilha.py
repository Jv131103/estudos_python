class FilaComPilhas:

    def __init__(self):
        self.entrada = []
        self.saida = []

    def enqueue(self, valor):
        self.entrada.append(valor)

    def dequeue(self):

        if not self.saida:

            while self.entrada:
                self.saida.append(self.entrada.pop())

        if not self.saida:
            raise IndexError("fila vazia")

        return self.saida.pop()

    def peek(self):

        if not self.saida:

            while self.entrada:
                self.saida.append(self.entrada.pop())

        return self.saida[-1]


f = FilaComPilhas()
f.enqueue(1)
f.enqueue(2)
f.enqueue(3)
f.enqueue(4)
f.enqueue(5)
print(f.dequeue())
print(f.peek())
