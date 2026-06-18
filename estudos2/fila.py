class FilaVaziaError(Exception):
    pass


class Fila:
    def __init__(self) -> None:
        self.fila = []  # TODO: péssima decisão, mas ver alternmativa

    def enqueue(self, valor):
        self.fila.append(valor)

    def dequeue(self):
        if self.is_empty():
            raise FilaVaziaError("Fila vazia!")
        return self.fila.pop(0)  # O(n)

    def peek(self):
        if self.is_empty():
            raise FilaVaziaError("Fila vazia!")
        return self.fila[0]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.fila)

    def __str__(self) -> str:
        return f"Fila(queue={self.fila}, first={self.peek()}, last={self.fila[-1]}, empty={self.is_empty()})"


fila = Fila()
fila.enqueue('a')
fila.enqueue('b')
fila.enqueue('c')
fila.enqueue('d')
print(fila)
print(fila.dequeue())
print(fila.dequeue())
print(fila)
