def subtracao(n1, n2):
    return n1 - n2


def saida_final(resultado):
    if resultado > 0:
        return "Resultado positivo"
    elif resultado < 0:
        return "Resultado negativo"
    else:
        return "Zero"


n1 = int(input())
n2 = int(input())

resultado = subtracao(n1, n2)

print(saida_final(resultado))
