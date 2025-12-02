class Deque:
    def __init__(self) -> None:
        self.valor = []

    def tamanho(self):
        return len(self.valor)

    def esta_vazio(self):
        return self.tamanho() == 0

    def add_final(self, valor):
        self.valor.append(valor)

    def add_inicio(self, valor):
        self.valor.insert(0, valor)

    def remove_final(self):
        if self.esta_vazio():
            print("Erro, a lista está vazia")
            return
        return self.valor.pop()

    def remove_inicio(self):
        if self.esta_vazio():
            print("Erro, a lista está vazia")
            return
        return self.valor.pop(0)

    def __repr__(self) -> str:
        return f"Deque({self.valor})"


if __name__ == "__main__":
    d = Deque()
    d.add_final(10)
    d.add_inicio(5)
    d.add_final(20)

    print(d)                  # Deque([5, 10, 20])
    print(d.remove_inicio())  # 5
    print(d.remove_final())   # 20
    print(d.tamanho())        # 1
