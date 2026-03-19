class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if not self.tail:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None

        value = self.head.data
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return value

    def peek(self):
        if not self.head:
            return None

        return self.head.data

    def is_empty(self):
        return self.head is None


lista = QueueLinkedList()
lista.enqueue(10)
lista.enqueue(20)
lista.enqueue(30)
lista.enqueue(40)
print(lista.peek())
print(lista.dequeue())
print(lista.peek())
print(lista.is_empty())
