class Livro:
    def __init__(self, titulo, autor, preco, qtd_estoque) -> None:
        self.titulo = titulo
        self.autor = autor
        self.__preco = float(preco)
        self.__qtd_estoque = int(qtd_estoque)

    def vender(self, qtd: int):
        if qtd <= 0:
            print("Quantidade inválida para venda.")
            return

        if not self.em_estoque():
            print("Produto indisponível no estoque, por favor compre outro produto")
            print(f"Estoque: {self.__qtd_estoque}")
            return

        if qtd > self.__qtd_estoque:
            print("Estoque insuficiente, por favor compre até o limite do estoque")
            print(f"Estoque disponível: {self.__qtd_estoque}")
            return

        self.__qtd_estoque -= qtd

    def repor(self, qtd: int):
        if qtd <= 0:
            print("Quantidade inválida para repor estoque")
            return

        self.__qtd_estoque += qtd

    def em_estoque(self) -> bool:
        return self.__qtd_estoque > 0

    @property
    def preco(self) -> float:
        return self.__preco

    @property
    def valor_total_estoque(self) -> float:
        return self.__preco * self.__qtd_estoque

    def __str__(self) -> str:
        info = f"título='{self.titulo}', autor='{self.autor}'"
        resp = (
            f"Estoque: {self.__qtd_estoque}, "
            f"Preço unitário: R$ {self.__preco:.2f}, "
            f"Valor em estoque: R$ {self.valor_total_estoque:.2f}"
        )
        return f"LIVRO({info} | {resp})"


l = Livro("1984", "George Orwell", 45.90, 10)
l.vender(3)
print(l)
l.repor(5)
print(l.em_estoque())  # True
