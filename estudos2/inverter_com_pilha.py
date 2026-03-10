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


string = "Python"
inverso = []

p = Pilha()

for char in string:
    p.push(char)

while not p.is_empty():
    inverso.append(p.pop())

print("".join(inverso))
