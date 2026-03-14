class FilaCircular:

    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.head = 0
        self.tail = 0
        self.count = 0
        self.tamanho = tamanho

    def enqueue(self, valor):
        if self.is_full():
            raise Exception("Fila cheia")

        self.vetor[self.tail] = valor

        self.tail = (self.tail + 1) % self.tamanho

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila vazia")

        valor = self.vetor[self.head]

        self.head = (self.head + 1) % self.tamanho

        self.count -= 1

        return valor

    def peek(self):
        if self.is_empty():
            raise Exception("Fila vazia")

        return self.vetor[self.head]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.tamanho

    def size(self):
        return self.count

    def __str__(self) -> str:
        elementos = []

        for i in range(self.count):
            pos = (self.head + i) % self.tamanho
            elementos.append(str(self.vetor[pos]))

        return " ".join(elementos)


if __name__ == "__main__":
    fc = FilaCircular(3)

    fc.enqueue(10)
    fc.enqueue(20)
    fc.enqueue(30)

    print(fc)

    fc.dequeue()
    fc.enqueue(40)

    print(fc)
