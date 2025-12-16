class Produtos:
    def __init__(self, nome, preco, quantidade) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto):
        if not isinstance(produto, Produtos):
            print("Objeto referenciado precisa ser um Produto")
            return
        self.produtos.append(produto)

    def remover_produto(self, nome):
        if not self.produtos:
            print("Carrinho vazio!")
            return
        for produtos in self.produtos:
            if produtos.nome == nome:
                print(f"Produto {nome} removido com sucesso")
                self.produtos.remove(produtos)
                return
        print("Produto não encontrado!")
        return

    def total(self):
        soma = 0
        for produtos in self.produtos:
            soma += produtos.total()

        return soma


p1 = Produtos("Laptop", 3000, 1)
p2 = Produtos("Teclado", 200.5, 2)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
print(carrinho.total())
carrinho.remover_produto("Teclado")
print(carrinho.total())
