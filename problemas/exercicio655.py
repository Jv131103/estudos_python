"""
Crie uma classe Carrinho com __len__.
"""


class Carrinho:
    def __init__(self) -> None:
        self.carrinho = []

    def add(self, produto):
        self.carrinho.append(produto)

    def __len__(self):
        return len(self.carrinho)


car1 = Carrinho()
car1.add("1")
car1.add("2")
print(len(car1))
