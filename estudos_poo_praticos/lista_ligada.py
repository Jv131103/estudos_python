from typing import Any


class No:
    def __init__(self, valor) -> None:
        self.valor: Any = valor
        self.proximo: Any = None


class ListaLigada:
    def __init__(self) -> None:
        self.head: No | None = None

    def adicionar_no_inicio(self, valor):
        no = No(valor)
        no.proximo = self.head
        self.head = no

    def adicionar_no_fim(self, valor):
        novo = No(valor)
        if self.head is None:
            self.head = novo
            return

        dado = self.head
        while dado.proximo:
            dado = dado.proximo

        dado.proximo = novo

    def imprimir(self):
        valores = self.head

        while valores:
            print(valores.valor)
            valores = valores.proximo


lista = ListaLigada()
lista.adicionar_no_fim(30)
lista.adicionar_no_fim(20)
lista.adicionar_no_fim(10)
lista.imprimir()
print()
lista.adicionar_no_inicio(30)
lista.adicionar_no_inicio(20)
lista.adicionar_no_inicio(10)
lista.imprimir()
