class Pilha:
    def __init__(self) -> None:
        self.pilha = []

    def vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        return len(self.pilha)

    def topo(self):
        if self.vazia():
            print("Pilha Vazia")
            return -1
        return self.pilha[len(self.pilha) - 1]

    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if self.vazia():
            print("Pilha Vazia")
            return
        return self.pilha.pop()

    def __repr__(self) -> str:
        return f"Pilha({self.pilha})"


if __name__ == "__main__":
    p = Pilha()
    p.empilhar(10)
    p.empilhar(20)
    p.empilhar(30)

    print(p)
    print(p.desempilhar())
    print(p.topo())
    print(p.tamanho())
