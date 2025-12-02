from exercicio179 import Pilha


def validar(expressao):
    p = Pilha()

    for ch in expressao:
        # Caracter de abertura
        if ch in "([{":
            p.empilhar(ch)

        # Caracter de fechamento
        elif ch in ")]}":
            # Não pode fechar sem antes abrir
            if p.vazia():
                return False

            topo = p.desempilhar()

            # Confere se combina o par
            if ch == ')' and topo != '(':
                return False
            if ch == ']' and topo != '[':
                return False
            if ch == '}' and topo != '{':
                return False

    # No final, nada pode ficar aberto
    return p.vazia()


print(validar("()"))
print(validar("([])"))
print(validar("{[()]}"))
print(validar("([)]"))
print(validar("(]"))
print(validar("{([])}"))
print(validar("(((()))"))
