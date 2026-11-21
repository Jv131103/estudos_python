
class Produto:
    def __init__(self, preco):
        self.__preco = 0
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, bool) or not isinstance(novo_preco, (int, float)):
            raise TypeError("Preço precisa ser numérico")

        if novo_preco <= 0:
            raise ValueError("Preço precisa ser positivo")

        self.__preco = novo_preco


produto = Produto(3500)

print(produto.preco)

produto.preco = 4000

print(produto.preco)
