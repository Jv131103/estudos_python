class Deque:
    def __init__(self) -> None:
        self.dados = []

    def append_left(self, valor):
        self.dados.insert(0, valor)

    def append_right(self, valor):
        self.dados.append(valor)

    def pop_left(self):
        if self.is_empty():
            raise ValueError("Fila Vazia")
        return self.dados.pop(0)

    def pop_right(self):
        if self.is_empty():
            raise ValueError("Fila Vazia")
        return self.dados.pop()

    def peek_front(self):
        if self.is_empty():
            return -1
        return self.dados[0]

    def peek_back(self):
        if self.is_empty():
            return -1
        return self.dados[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.dados)


if __name__ == "__main__":
    deque = Deque()
    deque.append_right(10)
    deque.append_right(20)
    deque.append_left(5)
    print(deque.dados)
    print(deque.peek_back(), deque.peek_front())

    remover_equerda, remover_direita = deque.pop_left(), deque.pop_right()
    print(remover_equerda, remover_direita)
    print(deque.dados)
