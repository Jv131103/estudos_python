class FilaCircular:
    def __init__(self, tamanho) -> None:
        if tamanho <= 0:
            raise ValueError("tamanho deve ser >= 1")

        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.inicio = 0
        self.fim = 0
        self.qtd = 0  # quantos elementos válidos estão na fila

    def vazia(self):
        return self.qtd == 0

    def cheia(self):
        return self.qtd == self.tamanho

    def enqueue(self, valor):
        if self.cheia():
            raise IndexError("Fila cheia")

        self.fila[self.fim] = valor
        self.fim = (self.fim + 1) % self.tamanho
        self.qtd += 1

    def dequeue(self):
        if self.vazia():
            raise IndexError("Fila vazia")

        valor = self.fila[self.inicio]
        self.fila[self.inicio] = None  # opcional: ajuda a visualizar/debugar
        self.inicio = (self.inicio + 1) % self.tamanho
        self.qtd -= 1
        return valor


f = FilaCircular(3)
f.enqueue(10)
f.enqueue(20)
f.enqueue(30)
print(f.dequeue())
