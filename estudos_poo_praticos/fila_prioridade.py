class PriorityQueue:
    def __init__(self):
        self.dados = []

    def push(self, valor, prioridade):
        self.dados.append((prioridade, valor))

    def pop(self):

        maior = 0

        for i in range(1, len(self.dados)):
            if self.dados[i][0] < self.dados[maior][0]:
                maior = i

        prioridade, valor = self.dados.pop(maior)
        return valor

    def priority(self):
        maior = 0

        for i in range(1, len(self.dados)):
            if self.dados[i][0] < self.dados[maior][0]:
                maior = i

        return self.dados[maior]


f = PriorityQueue()
f.push("A", 4)
f.push("B", 3)
f.push("C", 2)
f.push("D", 1)
f.push("E", 5)
print(f.pop())
print(f.priority())
