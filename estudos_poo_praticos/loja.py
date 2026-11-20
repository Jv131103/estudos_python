from produto2 import Produto


class Loja:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError("produto precisa ser do tipo Produto")

        self.produtos.append(produto)

    def calcular_valor_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.calcular_valor_estoque()

        return soma


loja = Loja()

loja.adicionar_produto(Produto("Mouse", 50, 10))
loja.adicionar_produto(Produto("Teclado", 120, 5))
loja.adicionar_produto(Produto("Monitor", 900, 3))

print(loja.calcular_valor_total())
