class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Produto precisa ser do Tipo <Produto>")
        self.produtos.append(produto)

    def remover(self, produto):
        if not isinstance(produto, Produto):
            raise ValueError("Produto precisa ser do Tipo <Produto>")
        self.produtos.remove(produto)

    def total(self):
        soma = 0
        for produtos in self.produtos:
            soma += produtos.get_preco()

        return soma

    def listar(self):
        for produtos in self.produtos:
            print("==" * 20)
            print(f"Produto: {produtos.get_nome()}")
            print(f"Valor: {produtos.get_preco():.2f}")
            print("==" * 20)


p1 = Produto("Mouse", 80)
p2 = Produto("Teclado", 150)

c = CarrinhoDeCompras()
c.adicionar(p1)
c.adicionar(p2)

print(c.total())  # 230
c.listar()

c.remover(p1)
c.listar()
