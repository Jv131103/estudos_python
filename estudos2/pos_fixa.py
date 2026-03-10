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


def avaliar(expr):

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


entrada = "2 3 +"
print(avaliar(entrada))

entrada = "5 1 2 + 4 * + 3 -"
print(avaliar(entrada))

entrada = "3 3 /"
print(avaliar(entrada))
