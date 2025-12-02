def aplicar_operador(operadores, valores):
    op = operadores.pop()
    b = valores.pop()
    a = valores.pop()

    if op == '+':
        valores.append(a + b)
    elif op == '-':
        valores.append(a - b)
    elif op == '*':
        valores.append(a * b)
    elif op == '/':
        valores.append(a / b)  # divisão real


precedencia = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def avaliar_expressao(expr: str):
    valores = []     # pilha de números
    operadores = []  # pilha de operadores

    i = 0
    n = len(expr)

    while i < n:
        ch = expr[i]

        # Ignorar espaços
        if ch == ' ':
            i += 1
            continue

        # Se for número (pode ter vários dígitos)
        if ch.isdigit():
            num = 0
            while i < n and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            valores.append(num)
            continue  # já avançamos i dentro do while interno

        # Se for parêntese abrindo
        if ch == '(':
            operadores.append(ch)
            i += 1
            continue

        # Se for parêntese fechando
        if ch == ')':
            # Resolver tudo até achar '('
            while operadores and operadores[-1] != '(':
                aplicar_operador(operadores, valores)
            operadores.pop()  # remove o '('
            i += 1
            continue

        # Se for operador +, -, *, /
        if ch in '+-*/':
            # Enquanto o topo da pilha tiver operador com precedência
            # maior ou igual, aplica
            while (operadores and operadores[-1] != '('
                   and precedencia[operadores[-1]] >= precedencia[ch]):
                aplicar_operador(operadores, valores)

            operadores.append(ch)
            i += 1
            continue

        # Se chegar aqui, tem caractere inválido
        raise ValueError(f"Caractere inválido na expressão: {ch!r}")

    # Aplicar o que sobrou
    while operadores:
        aplicar_operador(operadores, valores)

    return valores[-1]


print(avaliar_expressao("2 + 3 * 4"))              # 14
print(avaliar_expressao("(2 + 3) * 4"))            # 20
print(avaliar_expressao("10 + 2 * 6"))             # 22
print(avaliar_expressao("100 * (2 + 12) / 14"))    # 100.0
