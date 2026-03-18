from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class ListaDupla:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def inserir_inicio(self, valor):
        novo = Node(valor)
        if not self.head:
            self.head = novo
            self.tail = novo
            return
        novo.next = self.head
        self.head.prev = novo
        self.head = novo

    def inserir_final(self, valor):
        novo = Node(valor)
        if not self.tail:
            self.head = novo
            self.tail = novo
            return
        self.tail.next = novo
        novo.prev = self.tail
        self.tail = novo

    def remover(self, valor):
        if self.head is None:
            return print("Lista vazia")

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        if self.head.valor == valor:
            self.head = self.head.next
            self.head.prev = None  # type: ignore

        elif self.tail.valor == valor:
            self.tail = self.tail.prev
            self.tail.next = None  # type: ignore

        else:
            atual = self.head
            while atual:
                if atual.valor == valor:
                    atual.prev.next = atual.next  # type: ignore
                    atual.next.prev = atual.prev  # type: ignore
                    return
                atual = atual.next
            print("Valor não encontrado")

    def __str__(self) -> str:
        if not self.head:
            return "Lista vazia"
        nodes = []
        atual = self.head
        while atual:
            nodes.append(str(atual.valor))
            atual = atual.next
        return "None ← " + " ↔ ".join(nodes) + " → None"


ld = ListaDupla()

ld.inserir_final(10)
ld.inserir_final(20)
ld.inserir_final(30)
ld.inserir_inicio(5)
ld.inserir_inicio(1)
print("Montada:     ", ld)

ld.remover(1)
print("Rem. início: ", ld)

ld.remover(30)
print("Rem. final:  ", ld)

ld.remover(10)
print("Rem. meio:   ", ld)

ld.remover(5)
print("Sobrou 1:    ", ld)

ld.remover(20)
print("Vazia:       ", ld)

ld.remover(99)
ld.inserir_inicio(42)
ld.remover(99)
print("Só o 42:     ", ld)
ld.remover(99)
print("Só o 42:     ", ld)
