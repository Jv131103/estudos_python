class Fila:
    def __init__(self) -> None:
        self.fila = []
        self.inicio = 0
        self.fim = 0
        self.limite_inicio = 10

    def is_empty(self):
        return self.inicio == self.fim

    def enqueue(self, valor):
        self.fila.append(valor)
        self.fim += 1

    def dequeue(self):
        if self.is_empty():
            return None

        removido = self.fila[self.inicio]
        self.inicio += 1

        if self.inicio >= self.limite_inicio:
            self.fila = self.fila[self.inicio:self.fim]
            self.fim = self.fim - self.inicio
            self.inicio = 0

        return removido

    def __str__(self) -> str:
        return f"{self.fila[self.inicio:self.fim]}"


fila = Fila()
fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C")
fila.enqueue("D")
print(fila)
print(fila.dequeue())
print(fila.dequeue())
print(fila)
