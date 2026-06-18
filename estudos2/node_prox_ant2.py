class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.ant = None


nos = [Node(10), Node(20), Node(30), Node(40), Node(50)]

for i in range(1, len(nos)):
    nos[i].ant = nos[i-1]
    nos[i-1].prox = nos[i]

inicio = nos[0]   # ← primeiro da lista
fim = nos[-1]     # ← último da lista

print("Frente:")
atual = inicio
while atual:
    print(atual.valor)
    atual = atual.prox

print("\nTrás:")
atual = fim
while atual:
    print(atual.valor)
    atual = atual.ant
