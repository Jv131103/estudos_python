class Pilha:
    def __init__(self):
        self.pilha = []

    def isempty(self):
        return len(self.pilha) == 0

    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        if not self.isempty():
            return self.pilha.pop()
        return None

    def top(self):
        if self.isempty():
            return None
        return self.pilha[-1]


p = Pilha()
p.push('a')
p.push('b')
p.push('c')
print(p.top())
print(p.pop())
print(p.top())
