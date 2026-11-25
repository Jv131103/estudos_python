class Produto:
    def __init__(self, nome, preco=0.0) -> None:
        self.nome = nome
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if not isinstance(novo_preco, (int, float)) or isinstance(novo_preco, bool):
            raise TypeError("Tipo inválido para novo preço")

        if novo_preco < 0:
            raise ValueError("novo_preco não pode obter valores negativos")

        self.__preco = novo_preco


class Carrinho:
    def __init__(self) -> None:
        self.carrinho = {}

    def adicionar(self, produto, quantidade):
        if not isinstance(produto, Produto):
            raise TypeError("Produto precisa ser do tipo produto")

        if not isinstance(quantidade, int) or isinstance(quantidade, bool):
            raise TypeError("Quantidade precisa ser do tipo Inteiro")

        if quantidade <= 0:
            raise ValueError("Quantidade precisa ser > 0")

        self.carrinho[produto] = self.carrinho.get(produto, 0) + quantidade

    def total(self):
        soma = 0
        for produto, qtd in self.carrinho.items():
            soma += qtd * produto.preco

        return soma


produtos = [
    [Produto("Mouse", 150.50), 2],
    [Produto("Teclado", 200), 1]
]

carrinho = Carrinho()
for produto, quantidade in produtos:
    carrinho.adicionar(produto, quantidade)

print(f"Total: R$ {carrinho.total():.2f}")


mouse = Produto("Mouse", 150.50)

carrinho = Carrinho()
carrinho.adicionar(mouse, 2)
carrinho.adicionar(mouse, 3)

print(carrinho.total())
