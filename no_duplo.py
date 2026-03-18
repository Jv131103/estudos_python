from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


def percorrer_para_frente(node):
    current = node

    while current:
        print(current.valor)
        current = current.next


def percorrer_para_tras(node):
    current = node

    while current:
        print(current.valor)
        current = current.prev


def inserir_no_meio(node_inicio: Node, node_fim: Node, valor: Any):
    novo = Node(valor)

    novo.prev = node_inicio
    novo.next = node_fim

    node_inicio.next = novo
    node_fim.prev = novo

    # Verificando a corrente completa
    print(node_inicio.valor)             # 10
    print(node_inicio.next.valor)        # 30
    if node_inicio.next.next:
        print(node_inicio.next.next.valor)   # 50
    print()
    # Voltando
    print(node_fim.valor)             # 50
    print(node_fim.prev.valor)        # 30
    if node_fim.prev.prev:
        print(node_fim.prev.prev.valor)   # 10


if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    # conectar ida
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    # conectar volta
    n2.prev = n1
    n3.prev = n2
    n4.prev = n3
    n5.prev = n4

    print(n1.valor)
    print(n2.valor)
    print(n1.next.valor)
    print(n2.prev.valor)
    print()

    percorrer_para_frente(n1)
    print()
    percorrer_para_tras(n5)
    print()
    inserir_no_meio(n1, n5, 30)
    inserir_no_meio(n1, n5, 30)
