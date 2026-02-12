class Vetor:
    def __init__(self, n1, n2) -> None:
        self.n1 = n1
        self.n2 = n2

    def __add__(self, outro):
        return Vetor(self.n1 + outro.n1, self.n2 + outro.n2)

    def __repr__(self):
        return f"Vetor({self.n1}, {self.n2})"


v1 = Vetor(2, 3)
v2 = Vetor(4, 5)

v3 = v1 + v2
print(v3)
