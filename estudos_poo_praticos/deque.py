class Deque:
    def __init__(self):
        self.dados = []

    def append_right(self, valor):
        self.dados.append(valor)

    def append_left(self, valor):
        self.dados.insert(0, valor)

    def pop_right(self):
        return self.dados.pop()

    def pop_left(self):
        return self.dados.pop(0)


d = Deque()
d.append_right(1)
d.append_right(2)
d.append_right(3)
d.append_right(4)
d.append_left(1)
d.append_left(2)
d.append_left(3)
print(d.dados)
print(d.pop_left())
print(d.pop_right())
print(d.dados)
