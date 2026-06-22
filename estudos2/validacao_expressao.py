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
        # Só chama o peek() se a pilha NÃO estiver vazia, caso contrário exibe None
        topo = self.peek() if not self.is_empty() else None
        return f"Pilha(stack={self.pilha}, peek={topo}, empty={self.is_empty()})"


def validar_parentesis(expressao):
    p = Pilha()
    mapeamento = {")": "(", "]": "[", "}": "{"}
    for exp in expressao:
        if exp in "([{":
            p.push(exp)
        elif exp in ")]}":
            if p.is_empty():
                return False

            topo = p.pop()

            if topo != mapeamento[exp]:
                return False

    if p.is_empty():
        return True
    return False


print(validar_parentesis("()"))
print(validar_parentesis("("))
print(validar_parentesis(")"))
print(validar_parentesis("[]"))
print(validar_parentesis("{}"))
print(validar_parentesis("[{}]"))
print(validar_parentesis("([{}])"))
print(validar_parentesis("[{}"))
print(validar_parentesis("{}]"))
print(validar_parentesis("([)]"))
