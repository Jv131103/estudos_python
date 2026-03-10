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


def verificar(string):
    p = Pilha()

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for key in string:
        if key in ["{", "(", "["]:
            p.push(key)
        elif key in ["}", ")", "]"]:
            if p.is_empty():
                return False

            topo = p.pop()

            if topo != pares[key]:
                return False

    return p.is_empty()


def verificar2(string):
    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    dados = []

    for char in string:
        if char in "({[":
            dados.append(char)
        elif char in ")}]":
            if not dados:
                return False

            topo = dados.pop()

            if topo != pares[char]:
                return False

    return len(dados) == 0


def verificar3(string):

    while "()" in string or "{}" in string or "[]" in string:
        string = string.replace("()", "")
        string = string.replace("{}", "")
        string = string.replace("[]", "")

    return string == ""


def verificar4(s):

    pilha = []
    pares = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for c in s:

        if c in pares:
            pilha.append(pares[c])

        else:
            if not pilha or pilha.pop() != c:
                return False

    return not pilha


if __name__ == "__main__":
    print(verificar("[()]"))
    print(verificar2("[()]"))
    print(verificar3("[()]"))
    print(verificar4("[()]"))
