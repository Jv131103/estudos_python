class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * percentual / 100
        return self.preco

    def __str__(self) -> str:
        return f"Produto(nome={self.nome}, preco={self.preco:.2f})"


p = Produto("Notebook", 5000)
p.aplicar_desconto(10)
print(p)   # Produto(nome='Notebook', preco=4500.00)
