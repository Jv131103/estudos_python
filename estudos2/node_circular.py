class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __str__(self) -> str:
        return str(self.valor)


a = Node(1)
b = Node(2)
c = Node(3)

a.proximo = b
b.proximo = c
c.proximo = a

print(a)
print(a.proximo)
print(b)
print(b.proximo)
print(c)
print(c.proximo)
