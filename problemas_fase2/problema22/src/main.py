class Fila:
    def __init__(self) -> None:
        self.dados = []

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.dados[0]

    def size(self):
        return len(self.dados)

    def enqueue(self, valor):
        self.dados.append(valor)

    def dequeue(self):
        if self.is_empty():
            return print("FILA VAZIA")
        return self.dados.pop(0)


if __name__ == "__main__":
    f = Fila()
    f.enqueue(10)
    f.enqueue(20)
    f.enqueue(30)
    print(f.dequeue())
    print(f.peek())
