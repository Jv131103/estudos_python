class PilhaMin:
    def __init__(self):
        self.pilha = []
        self.auxiliar = []

    def is_empty(self):
        return len(self.pilha) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.pilha[-1]

    def push(self, valor):
        self.pilha.append(valor)
        if not self.auxiliar or valor <= self.auxiliar[-1]:
            self.auxiliar.append(valor)

    def pop(self):
        if self.is_empty():
            return None

        topo = self.pilha.pop()
        if topo == self.auxiliar[-1]:
            self.auxiliar.pop()
        return topo

    def get_min(self):
        if self.is_empty():
            return None
        return self.auxiliar[-1]


p = PilhaMin()
p.push(2)
p.push(2)
p.push(1)
p.push(1)

print(p.get_min())
print(p.pop())
print(p.get_min())
print(p.pop())
print(p.get_min())
