class Pilha:

    def __init__(self):
        self.dados = []

    def push(self, valor):
        self.dados.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.dados.pop()

    def peek(self):
        if not self.is_empty():
            return self.dados[-1]

    def is_empty(self):
        return len(self.dados) == 0

    def __str__(self) -> str:
        return " -> ".join(map(str, self.dados[:-1])) + f" -> {self.dados[-1]} [PEEK]"


p = Pilha()
p.push(1)
p.push(2)
p.push(3)
p.push(4)
p.push(5)
print(p)
print(p.pop())
print(p)
print(p.peek())
print(p.is_empty())
