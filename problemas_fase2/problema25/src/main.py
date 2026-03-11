class FilaComPilha:
    def __init__(self) -> None:
        self.entrada = []
        self.saida = []

    def enqueue(self, valor):
        self.entrada.append(valor)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("fila vazia")

        if not self.saida:
            while self.entrada:
                self.saida.append(self.entrada.pop())

        return self.saida.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("fila vazia")

        if not self.saida:
            while self.entrada:
                self.saida.append(self.entrada.pop())

        return self.saida[-1]

    def is_empty(self):
        return len(self.entrada) == 0 and len(self.saida) == 0

    def size(self):
        return len(self.entrada) + len(self.saida)


if __name__ == "__main__":
    fp = FilaComPilha()
    fp.enqueue(10)
    fp.enqueue(20)
    fp.enqueue(30)

    print(fp.dequeue())
    print(fp.peek())
    print(fp.size())
