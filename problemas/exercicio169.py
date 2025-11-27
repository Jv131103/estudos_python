class Lista:
    def __init__(self):
        self.lista = []

    def __esta_vazia(self):
        return self.tamanho_lista() == 0

    def adicionar_inicio(self, valor):
        self.lista.insert(0, valor)

    def adicionar_fim(self, valor):
        self.lista.append(valor)

    def remover_elemento(self, valor):
        if self.__esta_vazia():
            print("Lista vazia, não haverá remoções")
            return
        self.lista.pop(self.lista.index(valor))

    def tamanho_lista(self):
        return len(self.lista)

    def imprimir_elementos(self):
        for valores in self.lista:
            print(valores)
            print()

    def esvaziar_lista(self):
        if self.__esta_vazia():
            print("LISTA JÁ ESTÁ VAZIA")
        self.lista = []

    def __repr__(self) -> str:
        return f"Lista(tamanho={self.tamanho_lista()}, {self.lista})"

    def __str__(self) -> str:
        return f"{self.lista}"


if __name__ == "__main__":
    lista = Lista()
    lista.adicionar_fim(10)
    lista.adicionar_fim(10)
    lista.adicionar_inicio(20)
    print(lista)
    lista.remover_elemento(20)
    lista.imprimir_elementos()
    lista.esvaziar_lista()
    print(lista)
