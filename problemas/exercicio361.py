class Produto:
    def __init__(self, nome, preco, qtd) -> None:
        self.nome = nome
        self.qtd = qtd
        self.preco = preco
        self.total = self.preco * self.qtd


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.carrinho = []

    def adicionar_itens(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise ValueError("produto dever ser do tipo Produto")
        self.carrinho.append(produto)

    def remover_item(self, nome):
        for idx, produto in enumerate(self.carrinho):
            if produto.nome == nome:
                self.carrinho.pop(idx)
                return
        else:
            raise ValueError(f"{nome} não foi encontrado no carrinho")

    def total(self):
        soma = 0
        for produto in self.carrinho:
            soma += produto.total
        return soma

    def resumo(self):
        print("==" * 30)
        for produto in self.carrinho:
            print(f"Item {produto.nome} - R$ {produto.total:.2f}")
            print("--" * 30)
        print(f"Total: {self.total():.2f}")
        print("==" * 30)


processador = Produto("Processador Intel Core I12 12° geração", 2500, 1)
memoria_ram = Produto("Memória RAM DD4 8GB", 360, 2)
placa_mae = Produto("Placa mãe ASUS", 2000, 1)

carrinho = CarrinhoDeCompras()
carrinho.adicionar_itens(processador)
carrinho.adicionar_itens(memoria_ram)
carrinho.adicionar_itens(placa_mae)
carrinho.resumo()
carrinho.remover_item(memoria_ram.nome)
carrinho.resumo()
