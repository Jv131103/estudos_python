class Produto:
    def __init__(self, nome, preco=0.0, quantidade=0) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade


mouse = Produto("Mouse", 50, 10)
teclado = Produto("Teclado", 120, 5)

total_mouse = mouse.calcular_valor_estoque()
print(f"Mouse: R$ {total_mouse:.2f}")

total_teclado = teclado.calcular_valor_estoque()
print(f"Teclado: R$ {total_teclado:.2f}")
