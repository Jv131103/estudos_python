class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class ListaEncadeada:
    def __init__(self) -> None:
        self.head = None

    def inserir_inicio(self, valor):
        novo = Node(valor)
        novo.next = self.head
        self.head = novo

    def inserir_final(self, valor):
        novo = Node(valor)

        if self.head is None:
            self.head = novo
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = novo

    def buscar(self, valor):
        current = self.head

        while current:
            if valor == current.data:
                return True
            current = current.next

        return False

    def encontrar_meio(self):
        if self.head is None:
            return None

        current = self.head

        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

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
        current = self.head

        novo = []
        while current:
            novo.append(str(current.data))
            current = current.next

        return " -> ".join(novo)
    
    def is_cicle(self):
        current = self.head

        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


li = ListaEncadeada()
li.inserir_final(10)
li.inserir_final(20)
li.inserir_final(30)
li.inserir_inicio(40)
li.inserir_inicio(50)
li.inserir_inicio(60)
print(li)
print(li.buscar(10), li.buscar(40))
print(li.encontrar_meio())
li.reverse()
print(li)

# Tornar cicle como True
segundo = li.head.next
ultimo = li.head

while ultimo.next:
    ultimo = ultimo.next

ultimo.next = segundo
print(li.is_cicle())
