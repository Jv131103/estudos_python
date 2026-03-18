from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_begin(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_begin(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_end(self):
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def __str__(self) -> str:
        if self.head is None:
            return "Lista vazia"

        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next

        return "None ← " + " ↔ ".join(nodes) + " → None"


ldi = DoublyLinkedList()
ldi.insert_begin(1)
ldi.insert_begin(2)
ldi.insert_begin(3)
ldi.insert_end(4)
ldi.insert_end(5)
ldi.insert_end(6)
print(ldi)
