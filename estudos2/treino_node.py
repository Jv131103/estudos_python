class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def imprimir_nodes(node):

    current = node

    while current:
        print(current.data)
        current = current.next


def imprimir_inverso(node):
    if node is None:
        return

    imprimir_inverso(node.next)
    print(node.data)


def contar_nodes(node):

    total = 0
    current = node

    while current:
        total += 1
        current = current.next

    return total


def fast_lazy_nodes(node):
    fast = node
    lazy = node

    while fast and fast.next:
        print(f"lazy: {lazy.data} | fast: {fast.data}")
        lazy = lazy.next
        fast = fast.next.next


if __name__ == "__main__":

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    imprimir_nodes(n1)

    total = contar_nodes(n1)
    print(f"Total de nodes: {total}")

    fast_lazy_nodes(n1)

    imprimir_inverso(n1)
