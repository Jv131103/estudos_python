class Pilha:
    def __init__(self) -> None:
        self.pilha = []

    def vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        return len(self.pilha)

    def topo(self):
        if self.vazia():
            return -1
        return self.pilha[len(self.pilha) - 1]

    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if self.vazia():
            return
        return self.pilha.pop()

    def __repr__(self) -> str:
        return f"Pilha({self.pilha})"


def validar_parentesis(dado):
    pilha = Pilha()

    for item in dado:
        if item == "(":
            pilha.empilhar(item)
        elif item == ")":
            if pilha.vazia():
                return "ERRO"
            pilha.desempilhar()

    if pilha.vazia():
        return "OK"

    return "ERRO"


def validar_parentesis2(s):
    saldo = 0
    for c in s:
        if c == "(":
            saldo += 1
        elif c == ")":
            saldo -= 1
            if saldo < 0:
                return "ERRO"
    return "OK" if saldo == 0 else "ERRO"


print(validar_parentesis("(()())"))  # OK
print(validar_parentesis("())("))    # ERRO
print(validar_parentesis(")("))      # ERRO
print(validar_parentesis("((())"))   # ERRO
print(validar_parentesis("()()()"))  # OK
print()
print(validar_parentesis2("(()())"))  # OK
print(validar_parentesis2("())("))    # ERRO
print(validar_parentesis2(")("))      # ERRO
print(validar_parentesis2("((())"))   # ERRO
print(validar_parentesis2("()()()"))  # OK
