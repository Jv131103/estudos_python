class PilhaIngenua:
    def __init__(self):
        self.dados = []

    def push(self, v):
        self.dados.append(v)

    def pop(self):
        return self.dados.pop()

    def get_min(self):
        return min(self.dados)
