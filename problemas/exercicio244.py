from exercicio240 import ListaEncadeada


class FilaEncadeada:
    def __init__(self) -> None:
        self.fila = ListaEncadeada()

    def enfileirar(self, valor):
        self.fila.adicionar_final(valor)

    def desenfileirar(self):
        if self.vazia():
            return None
        valor = self.fila.head.dado  # type:ignore
        self.fila.remover_inicio()
        return valor

    def primeiro(self):
        if self.vazia():
            return None
        return self.fila.head.dado  # type:ignore

    def vazia(self):
        return self.fila.head is None


f = FilaEncadeada()
f.enfileirar("A")
f.enfileirar("B")
print(f.primeiro())
print(f.desenfileirar())
print(f.desenfileirar())
print(f.vazia())
