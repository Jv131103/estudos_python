class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node    

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def delete_begin(self):

        if self.head is None:
            return None

        self.head = self.head.next
        return self.head

    def delete_end(self):

        if self.head is None:
            return None

        # caso tenha apenas 1 elemento
        if self.head.next is None:
            self.head = None
            return None

        current = self.head

        while current.next.next:
            current = current.next

        current.next = None
        return self.head

    def delete_value(self, value):

        if self.head is None:
            return None

        # se for o primeiro
        if self.head.data == value:
            self.head = self.head.next
            return self.head

        current = self.head

        while current.next:

            if current.next.data == value:
                current.next = current.next.next
                return self.head

            current = current.next

        return self.head

    def reverse(self):

        prev = None
        current = self.head

        while current:

            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        self.head = prev
        return self.head

    def __str__(self) -> str:

        elementos = []
        current = self.head

        while current:
            elementos.append(str(current.data))
            current = current.next

        return " -> ".join(elementos)


lista = LinkedList()

lista.insert_begin(10)
lista.insert_begin(5)
lista.insert_end(20)
lista.insert_end(30)

print(lista)

lista.delete_begin()
lista.delete_end()
lista.delete_value(10)

print(lista)

lista.insert_begin(10)
lista.insert_begin(5)
print(lista)

lista.reverse()
print(lista)
lista.reverse()
print(lista)
