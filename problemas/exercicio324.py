class Produto:
    def __init__(self, nome, preco, estoque) -> None:
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, qtd):
        if qtd <= 0:
            print("Não foi possível realizar compra, a qtd precisa ser maior que 0")
            return
        elif qtd > self.estoque:
            print("Qtd insuficiente no estoque")
            return

        self.estoque -= qtd
        return self.preco * qtd

    def repor(self, qtd):
        if qtd <= 0:
            print("Não foi possível repor estoque, a qtd precisa ser maior que 0")
            return

        self.estoque += qtd

    def aplicar_desconto(self, percentual=0):
        self.preco = self.preco - (self.preco * percentual / 100)
        return round(self.preco, 2)

    def __str__(self) -> str:
        return f"Produto(nome={self.nome}, preco(atual)={self.preco:.2f}, estoque={self.estoque})"


p1 = Produto("Hd Externo", 470.85, 100)
print(p1)
print(p1.vender(10))
print(p1)
p1.repor(10)
print(p1)
print(p1.aplicar_desconto(25))
p1.repor(10)
print(p1)
