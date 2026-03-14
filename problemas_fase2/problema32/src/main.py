class Pilha:

    def __init__(self):
        self.dados = []
        self.minimos = []

    def push(self, valor):

        self.dados.append(valor)

        if not self.minimos:
            self.minimos.append(valor)
        else:
            self.minimos.append(min(valor, self.minimos[-1]))

    def pop(self):

        if not self.dados:
            raise ValueError("Pilha vazia")

        self.minimos.pop()
        return self.dados.pop()

    def top(self):

        if not self.dados:
            raise ValueError("Pilha vazia")

        return self.dados[-1]

    def get_min(self):

        if not self.minimos:
            raise ValueError("Pilha vazia")

        return self.minimos[-1]


if __name__ == "__main__":
    p = Pilha()
    p.push(5)
    p.push(3)
    p.push(7)
    print(p.get_min())
    p.pop()
    print(p.get_min())
    p.pop()
    print(p.dados)
    print(p.get_min())
    p.push(10)
    p.push(5)
    print(p.get_min())
