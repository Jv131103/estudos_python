class Pilha:
    def __init__(self):
        self.pilha = []

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):   # remove e retorna o topo; erro se vazia
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar: pilha vazia")
        return self.pilha.pop()

    def topo(self):          # olha o topo sem remover; erro se vazia
        if self.esta_vazia():
            raise IndexError("Não é possível desempilhar: pilha vazia")
        return self.pilha[-1]

    def esta_vazia(self):
        return len(self.pilha) == 0


def parenteses_balanceados(expressao):
    # usa a Pilha pra verificar
    p = Pilha()

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for key in expressao:
        if key in ["{", "(", "["]:
            p.empilhar(key)
        elif key in ["}", ")", "]"]:
            if p.esta_vazia():
                return False

            topo = p.desempilhar()

            if topo != pares[key]:
                return False

    return p.esta_vazia()


print(parenteses_balanceados("(a + b) * (c - d)"))     # True
print(parenteses_balanceados("(a + b * (c - d)"))       # False (não fechou)
print(parenteses_balanceados("(a + b) * c - d)"))       # False (fechou sem abrir)
print(parenteses_balanceados("((a)(b))"))                # True
