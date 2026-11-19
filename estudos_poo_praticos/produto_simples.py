
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade

    def vender(self, quantidade_vendida):
        if quantidade_vendida <= 0:
            print("Venda não autorizada")
            print("A quantidade deve ser maior que zero.")
            return
        elif quantidade_vendida > self.quantidade:
            print("Venda não autorizada")
            print("Estoque insuficiente para realizar essa venda.")
            return

        self.quantidade -= quantidade_vendida
        return f"Venda realizada! Restam {self.quantidade} unidades."

    def __str__(self) -> str:
        return f"{self.nome} = R$ {self.calcular_valor_estoque():.2f}"


p = Produto("Carregador portátil", 38, 8)

valor_final = p.calcular_valor_estoque()
print(valor_final)
print(p)

print(p.vender(3))
print(p.quantidade)
print(p.calcular_valor_estoque())
