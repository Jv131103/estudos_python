def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao_real(a, b):
    return a / b if b != 0 else "Erro de divisão por 0"


def resto_divisao(a, b):
    return a % b if b != 0 else "Erro de divisão por 0"


def avaliar_postfix(expr):

    options = {
        "+": soma,
        "-": subtracao,
        "*": multiplicacao,
        "/": divisao_real,
        "%": resto_divisao
    }

    expr = expr.replace(' ', '')

    pilha = []

    for c in expr:

        if c.isdigit():
            pilha.append(int(c))

        else:

            b = pilha.pop()
            a = pilha.pop()

            if options.get(c):
                pilha.append(options[c](a, b))
            else:
                return print("Operador inválido!")

    return pilha.pop()


def avaliar_prefix(expr):

    pilha = []

    for c in reversed(expr.split()):

        if c.isdigit():
            pilha.append(int(c))

        else:
            a = pilha.pop()
            b = pilha.pop()

            if c == "+":
                pilha.append(a + b)
            elif c == "-":
                pilha.append(a - b)
            elif c == "*":
                pilha.append(a * b)
            elif c == "/":
                pilha.append(a / b)

    return pilha.pop()


if __name__ == "__main__":
    entrada = "2 3 +"
    print(avaliar_postfix(entrada))

    entrada = "5 1 2 + 4 * + 3 -"
    print(avaliar_postfix(entrada))

    entrada = "3 3 /"
    print(avaliar_postfix(entrada))
