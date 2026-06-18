class PilhaVaziaError(Exception):
    pass


class Pilha:
    def __init__(self) -> None:
        self.pilha = []

    def push(self, valor):
        self.pilha.append(valor)

    def pop(self):
        if self.is_empty():
            raise PilhaVaziaError("Pilha vazia!")
        return self.pilha.pop()

    def peek(self):
        if self.is_empty():
            raise PilhaVaziaError("Pilha vazia!")
        return self.pilha[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.pilha)

    def __str__(self) -> str:
        return f"Pilha(stack={self.pilha}, peek={self.peek()}, empty={self.is_empty()})"


pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
pilha.push(4)
print(pilha.pop())
pilha.push(5)
print(pilha)
print(pilha.pop())
print(pilha.pop())
print(pilha)
