class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.__preco = preco

    def desconto(self, percentual):
        if isinstance(percentual, float):
            percentual = percentual * 100
        return self.__preco - (self.__preco * percentual / 100)


p = Produto("Teclado", 100)
desconto = p.desconto(10)
print(desconto)
