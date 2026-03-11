class Fila:

    def __init__(self):
        self.dados = []

    def enqueue(self, valor):
        self.dados.append(valor)

    def dequeue(self):
        if not self.is_empty():
            return self.dados.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.dados[0]

    def is_empty(self):
        return len(self.dados) == 0

    def __str__(self) -> str:
        return f"[DEQUEUE] {self.dados[0]} <- " + " <- ".join(map(str, self.dados[1:-1])) + f" <- {self.dados[-1]} [ENQUEUE]"


f = Fila()
f.enqueue(1)
f.enqueue(2)
f.enqueue(3)
f.enqueue(4)
f.enqueue(5)
print(f)
print(f.dequeue())
print(f)
print(f.peek())
print(f.is_empty())
