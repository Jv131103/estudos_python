class Produto:
    def __init__(self, nome, codigo, preco=0.0) -> None:
        self.nome = nome
        self.codigo = codigo
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


class Estoque:
    def __init__(self) -> None:
        self.produtos = {}

    def cadastrar_produto(self, produto, quantidade):
        if not isinstance(produto, Produto):
            raise TypeError("produto precisa ser do tipo Produto")

        if not isinstance(quantidade, int) or isinstance(quantidade, bool):
            raise TypeError("quantidade deve ser do tipo INT")

        if quantidade <= 0:
            raise ValueError("Quantidade precisa ser maior que 0")

        if produto.codigo in self.produtos:
            if self.produtos[produto.codigo]["produto"].preco < produto.preco:
                self.produtos[produto.codigo]["produto"].preco = produto.preco

            self.produtos[produto.codigo]["quantidade"] += quantidade
            return

        self.produtos[produto.codigo] = {
            "produto": produto,
            "quantidade": quantidade
        }

    def exibir(self):
        for codigo, produto in self.produtos.items():
            print(f"Código: {codigo}")
            item, qtd = produto['produto'], produto['quantidade']
            print(f"Nome: {item.nome}")
            print(f"Preço: R$ {item.preco:.2f}")
            print(f"Quantidade: {qtd}")
            print()


prod1 = Produto("Mouse Gamer", "PRD001", 150.00)
prod2 = Produto("Mouse Gamer", "PRD001", 180.00)
estoque = Estoque()

estoque.cadastrar_produto(prod1, 5)
estoque.cadastrar_produto(prod2, 10)
estoque.exibir()
