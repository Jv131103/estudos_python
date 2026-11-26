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


mouse1 = Produto("mouse", 55)
mouse2 = Produto("mouse", 55)
referencia = mouse1

estoque = {}
estoque[mouse1] = 5
estoque[mouse2] = 10
print("Quantidade de chaves:", len(estoque))
print(mouse1 is mouse2)
print(mouse1 is referencia)
print(mouse2 is referencia)
