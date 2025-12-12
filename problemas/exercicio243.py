from exercicio240 import ListaEncadeada


class PilhaEncadeada:
    def __init__(self) -> None:
        self.fila = ListaEncadeada()

    def push(self, valor):
        self.fila.adicionar_inicio(valor)

    def pop(self):
        if self.vazia():
            return None
        valor = self.fila.head.dado  # type:ignore
        self.fila.remover_inicio()
        return valor

    def topo(self):
        if self.vazia():
            return None
        return self.fila.head.dado  # type:ignore

    def vazia(self):
        return self.fila.head is None


p = PilhaEncadeada()
p.push(10)
p.push(20)
print(p.topo())
print(p.pop())
print(p.pop())
print(p.vazia())
