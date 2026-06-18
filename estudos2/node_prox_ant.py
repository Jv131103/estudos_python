class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None


# Criação dos nós
a = Node(1)
b = Node(2)
c = Node(3)

# Ligação para frente
a.prox = b
b.prox = c

# Ligação para trás
b.ant = a
c.ant = b

# Referências importantes
inicio = a
fim = c

print("Percorrendo para frente:")
atual = inicio

while atual:
    print(atual.valor)
    atual = atual.prox

print("\nPercorrendo para trás:")
atual = fim

while atual:
    print(atual.valor)
    atual = atual.ant