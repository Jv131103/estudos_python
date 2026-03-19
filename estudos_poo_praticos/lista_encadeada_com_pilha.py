class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):

        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None

        value = self.top.data
        self.top = self.top.next

        return value

    def peek(self):
        if not self.top:
            return None

        return self.top.data

    def is_empty(self):
        return self.top is None


lista = StackLinkedList()
lista.push(10)
lista.push(20)
lista.push(30)
lista.push(40)
print(lista.peek())
print(lista.pop())
print(lista.is_empty())
print(lista.peek())
