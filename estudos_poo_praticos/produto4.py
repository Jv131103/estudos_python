
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def alterar_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
            return True

        return False

    def retornar_preco(self):
        return self.__preco

    def alterar_quantidade(self, nova_quantidade):
        if not isinstance(nova_quantidade, int) or isinstance(nova_quantidade, bool):
            raise ValueError("nova quantidade precisa ser do tipo INT")

        if nova_quantidade < 0:
            raise ValueError("nova quantidade não pode ser NEGATIVO")

        self.__quantidade = nova_quantidade

        return True

    def retornar_quantidade(self):
        return self.__quantidade


produto = Produto("Notebook", 3500, 5)

print(produto.alterar_preco(-500))
print(produto.retornar_preco())
print(produto.alterar_quantidade(3))
print(produto.retornar_quantidade())
