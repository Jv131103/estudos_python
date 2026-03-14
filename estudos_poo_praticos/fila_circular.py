class FilaCircular:

    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.head = 0
        self.tail = 0
        self.count = 0
        self.tamanho = tamanho

    def enqueue(self, valor):
        if self.count == self.tamanho:
            raise Exception("Fila cheia")

        self.vetor[self.tail] = valor

        self.tail = (self.tail + 1) % self.tamanho

        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Fila vazia")

        valor = self.vetor[self.head]

        self.head = (self.head + 1) % self.tamanho

        self.count -= 1

        return valor

    def peek(self):
        if self.count == 0:
            raise Exception("Fila vazia")

        return self.vetor[self.head]

    def __str__(self):
        elementos = []

        for i in range(self.count):
            pos = (self.head + i) % self.tamanho
            elementos.append(str(self.vetor[pos]))

        return "<- " + " <- ".join(elementos) + " <-"


f = FilaCircular(5)
f.enqueue(1)
f.enqueue(2)
f.enqueue(3)
f.enqueue(4)
f.enqueue(5)
print(f)
print(f.dequeue())
print(f.peek())
print(f)
print(f.dequeue())
print(f)
print(f.dequeue())
