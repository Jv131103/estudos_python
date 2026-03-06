class FilaCircular:

    def __init__(self, tamanho):
        self.vetor = [None] * tamanho
        self.head = 0
        self.tail = 0
        self.tamanho = tamanho
        self.quantidade = 0

    def enqueue(self, valor):

        if self.quantidade == self.tamanho:
            raise IndexError("fila cheia")

        self.vetor[self.tail] = valor
        self.tail = (self.tail + 1) % self.tamanho
        self.quantidade += 1

    def dequeue(self):

        if self.quantidade == 0:
            raise IndexError("fila vazia")

        valor = self.vetor[self.head]
        self.vetor[self.head] = None

        self.head = (self.head + 1) % self.tamanho
        self.quantidade -= 1

        return valor

    def __str__(self):

        elementos = []
        i = self.head

        for _ in range(self.quantidade):
            elementos.append(self.vetor[i])
            i = (i + 1) % self.tamanho

        return str(elementos)


if __name__ == "__main__":
    limite = 4

    fila = FilaCircular(limite)

    for i in range(limite):
        fila.enqueue(i)

    print(fila)
    print("Indice:", fila.dequeue())
    print(fila)

    fila.enqueue(4)
    print(fila)

    print("Indice:", fila.dequeue())
    print(fila)
