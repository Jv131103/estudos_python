class Vetor:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other):
        if not isinstance(other, Vetor):
            return NotImplemented
        return Vetor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vetor):
            return NotImplemented
        return Vetor(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar):
        if not isinstance(escalar, (int, float)):
            return NotImplemented
        return Vetor(self.x * escalar, self.y * escalar)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vetor(3, 4)
v2 = Vetor(1, 2)

v3 = v1 + v2
print(v3)
print(v3.magnitude())

print(v1 - v2)
print(v1 * 3)
