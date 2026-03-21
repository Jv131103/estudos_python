class Node:
    def __init__(self, valor):
        self.valor = valor
        self.filho = None


class ArvoreUnaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = Node(valor)

        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz

        while atual.filho is not None:
            atual = atual.filho

        atual.filho = novo

    def percorrer(self):
        atual = self.raiz

        while atual is not None:
            print(atual.valor)
            atual = atual.filho

    def exibir(self):
        current = self.raiz
        print(current.valor)
        while current.filho:
            print("|")
            print(current.filho.valor)

            current = current.filho


if __name__ == "__main__":
    a = ArvoreUnaria()
    a.inserir(10)
    a.inserir(5)
    a.inserir(2)
    a.inserir(0)
    a.exibir()
