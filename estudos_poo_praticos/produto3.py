
class Produto:
    def __init__(self, nome, preco=0.0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade

    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.quantidade:
            self.quantidade -= quantidade


mouse = Produto("Mouse", 50, 10)
teclado = Produto("Teclado", 120, 5)

mouse.adicionar_estoque(4)
teclado.vender(2)
mouse.vender(-2)

print("Mouse:", mouse.quantidade)
print("Teclado:", teclado.quantidade)
