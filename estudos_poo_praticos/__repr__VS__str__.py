class Produto:
    def __init__(self, nome, preco, qtd) -> None:
        if preco < 0:
            raise ValueError("Preço não pode ser negativo")
        if qtd < 0:
            raise ValueError("Quantidade não pode ser negativa")

        self.nome = nome
        self.__preco = preco
        self.__qtd = qtd

    @property
    def preco(self):
        return self.__preco

    @property
    def qtd(self):
        return self.__qtd

    def valor_total(self):
        return self.preco * self.qtd

    def __str__(self) -> str:
        return f"{self.nome} - R$ {self.preco:.2f} x {self.qtd} = R$ {self.valor_total():.2f}"

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome!r}, preco={self.preco}, qtd={self.qtd})"


p = Produto("Notebook", 3500.00, 2)
print(p)

produtos = [Produto("Notebook", 3500, 2), Produto("Mouse", 90, 1)]
print(produtos)
