def subtracao(n1, n2):
    return n1 - n2


def saida_final(resultado):
    match resultado:
        case 13 | 9 | -5 | -16:
            return f"Resultado é {resultado}"
        case _:
            return f"O resultado é diferente do anteriores: {resultado}"


n1 = int(input())
n2 = int(input())

resultado = subtracao(n1, n2)

print(saida_final(resultado))
