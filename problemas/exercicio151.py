class Produto:
    def __init__(self, nome, estoque, descricao, preco) -> None:
        self.nome = nome
        self.estoque = estoque
        self.descricao = descricao
        self.preco = preco

    def mostrar_nome(self):
        return self.nome

    def mudar_nome(self, novo_nome):
        self.nome = novo_nome

    def mostrar_descricao(self):
        return self.descricao

    def mudar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def mostrar_estoque(self):
        return self.estoque

    def mudar_estoque(self, novo_estoque):
        self.estoque = novo_estoque

    def mostrar_preco(self):
        return self.preco

    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

    def sumario(self):
        print(f"Nome......: {self.mostrar_nome()}")
        print(f"Descrição.: {self.mostrar_descricao()}")
        print(f"Estoque...: {self.mostrar_estoque()}")
        print(f"Preço.....: {self.mostrar_preco():.2f}")
        print()


produto = Produto("Notebook", 15, "Computador portátil", 5565.85)
produto.sumario()
produto.mudar_nome("Notebook Ryzen")
produto.mudar_descricao("Notebook Ryzen 5 - 12° geração")
produto.mudar_estoque(25)
produto.mudar_preco(5000)
produto.sumario()
