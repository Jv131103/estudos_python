def subtracao(n1, n2):
    return n1 - n2


def saida_final(resultado):
    if resultado in [1, 2, 3]:
        return f"Resultado é {resultado}"
    elif resultado in [-1, -2, -3]:
        return f"Resultado é {resultado}"
    else:
        return f"O resultado é diferente do anteriores: {resultado}"


n1 = int(input())
n2 = int(input())

resultado = subtracao(n1, n2)

print(saida_final(resultado))
