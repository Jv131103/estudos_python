def shunting_yard(expr):

    precedencia = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    saida = []
    pilha = []

    tokens = expr.split()

    for token in tokens:

        if token.isdigit():
            saida.append(token)

        elif token in precedencia:

            while (
                pilha
                and pilha[-1] in precedencia
                and precedencia[pilha[-1]] >= precedencia[token]
            ):
                saida.append(pilha.pop())

            pilha.append(token)

        elif token == "(":
            pilha.append(token)

        elif token == ")":

            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())

            pilha.pop()

    while pilha:
        saida.append(pilha.pop())

    return " ".join(saida)


def avaliar_postfix(expr):

    pilha = []

    for token in expr.split():

        if token.isdigit():
            pilha.append(int(token))

        else:

            b = pilha.pop()
            a = pilha.pop()

            if token == "+":
                pilha.append(a + b)
            elif token == "-":
                pilha.append(a - b)
            elif token == "*":
                pilha.append(a * b)
            elif token == "/":
                pilha.append(a / b)

    return pilha.pop()


expr = "3 + 4 * 2 / ( 1 - 5 )"

postfix = shunting_yard(expr)

resultado = avaliar_postfix(postfix)

print(postfix)
print(resultado)
