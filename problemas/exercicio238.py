class Pilha:
    def __init__(self) -> None:
        self.pilha = []

    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        if self.vazia():
            print("Pilha Vazia")
            return
        return self.pilha.pop()

    def topo(self):
        if self.vazia():
            print("Pilha Vazia")
            return
        return self.pilha[-1]

    def vazia(self):
        return len(self.pilha) == 0


p = Pilha()
p.push(10)
p.push(20)
print(p.topo())
print(p.pop())
print(p.pop())
print(p.vazia())
