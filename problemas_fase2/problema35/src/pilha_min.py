class PilhaMin:
    def __init__(self) -> None:
        self.pilha = []
        self.menores = []

    def push(self, valor):
        self.pilha.append(valor)
        if not self.menores:
            self.menores.append(valor)
        elif valor <= self.menores[-1]:
            self.menores.append(valor)

    def pop(self):
        if not self.is_empty():
            valor = self.pilha.pop()

            if valor == self.menores[-1]:
                self.menores.pop()

            return valor
        raise IndexError("pop de pilha vazia")

    def top(self):
        if not self.is_empty():
            return self.pilha[-1]
        raise IndexError("top de pilha vazia")

    def get_min(self):
        if not self.is_empty() and self.menores:
            return self.menores[-1]
        raise IndexError("get_min de pilha vazia")

    def is_empty(self):
        return len(self.pilha) == 0

    def __len__(self):
        return len(self.pilha)


if __name__ == "__main__":
    p = PilhaMin()
    p.push(10)
    p.push(0)
    p.push(25)
    p.push(12)
    p.push(-1)
    p.push(10)
    print(p.get_min())
    print(p.pop())
    print(p.get_min())
