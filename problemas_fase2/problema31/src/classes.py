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


class Pilha:

    def __init__(self):
        self.dados = []

    def push(self, valor):
        self.dados.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.dados.pop()

    def peek(self):
        if not self.is_empty():
            return self.dados[-1]

    def is_empty(self):
        return len(self.dados) == 0
