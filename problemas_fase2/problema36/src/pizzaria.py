class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"Nome: {self.nome} | Preço: R$ {self.preco:.2f}"


class Pizza(Produto):
    PRECOS = {"P": 25.0, "M": 35.0, "G": 45.0}

    def __init__(self, tamanho, sabores=None):
        if tamanho not in self.PRECOS:
            raise ValueError("Tamanho precisa ser P, M OU G")
        preco = self.PRECOS[tamanho]
        super().__init__(f"Pizza {tamanho}", preco)
        self.sabores = sabores if sabores is not None else []

    def adicionar_sabor(self, sabor):
        if len(self.sabores) >= 2:
            print("Limite de sabores atingido")
            return
        self.sabores.append(sabor)

    def descricao(self):
        if not self.sabores:
            return "Nenhum sabor pedido!"

        sabor = '/'.join(self.sabores)
        return f"🍕 {self.nome} - {sabor} - R$ {self.preco:.2f}"


class Bebida(Produto):
    def __init__(self, nome, preco, volume):
        super().__init__(f"{nome} {volume}", preco)

    def descricao(self):
        return f"🥤 {self.nome} - R$ {self.preco:.2f}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto):
        if not isinstance(produto, (Pizza, Bebida)):
            print("Digite apenas produtos do tipo Pizza ou Bebida")
            return
        self.itens.append(produto)

    def total(self):
        soma = 0
        for itens in self.itens:
            soma += itens.preco

        return f"Total: R$ {soma:.2f}"

    def resumo(self):
        print("===== PEDIDO =====")
        print(f"Cliente: {self.cliente}")
        print()
        for itens in self.itens:
            print(itens.descricao())
        print()
        print(self.total())
        print("==================")


if __name__ == "__main__":
    pizza_frango = Pizza("G", ["Frango", "Catupiry"])
    pizza_calabreza = Pizza("M", ["Calabresa"])
    coca_cola = Bebida("Coca-Cola", 6, "350ml")

    pedido = Pedido("João")
    pedido.adicionar_item(pizza_frango)
    pedido.adicionar_item(pizza_calabreza)
    pedido.adicionar_item(coca_cola)
    pedido.resumo()
