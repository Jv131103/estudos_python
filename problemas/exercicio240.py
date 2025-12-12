class Nodo:
    def __init__(self, dado) -> None:
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.head = None

    def adicionar_inicio(self, valor):
        no = Nodo(valor)
        if not self.head:
            self.head = no
        else:
            no.proximo = self.head  # type: ignore
            self.head = no

    def adicionar_final(self, valor):
        no = Nodo(valor)

        # caso lista vazia
        if not self.head:
            self.head = no
            return

        # percorrer até o último
        nodo = self.head
        while nodo.proximo is not None:
            nodo = nodo.proximo

        # agora nodo é o último
        nodo.proximo = no  # type: ignore

    def remover_inicio(self):
        if not self.head:
            return
        self.head = self.head.proximo

    def exibir(self):
        nodo = self.head
        while nodo is not None:
            print(f"{nodo.dado} -> ", end="")
            nodo = nodo.proximo
        print("None")

    def tamanho(self):
        cont = 0
        nodo = self.head
        while nodo is not None:
            cont += 1
            nodo = nodo.proximo
        return cont


if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.adicionar_inicio(10)
    lista.adicionar_inicio(20)
    lista.exibir()  # 20 -> 10
    lista.remover_inicio()
    lista.exibir()  # 10
    print(lista.tamanho())
