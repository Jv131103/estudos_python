def retornou_erro(op, n2):
    if op not in "+-*/":
        return "Operador inválido, os aceitáveis são: [+, -, *, /]"
    elif op == "/" and n2 == 0:
        return "Erro de divisão: O valor a direita não pode ser 0"
    return None


def calculate(n1, op, n2):
    erro = retornou_erro(op, n2)
    if erro:
        return erro
    return eval(f"{n1} {op} {n2}")  # isso é para fins didáticos, nunca use isso em prod


while True:
    try:
        n1 = int(input("N1: "))
    except ValueError:
        print("Erro, N1 deve ser do tipo numérico")
        continue
    op = input("Operador [+, -, *, /]: ")
    try:
        n2 = int(input("N2: "))
    except ValueError:
        print("Erro, N2 deve ser do tipo numérico")
        continue
    print(calculate(n1, op, n2))
    continuar = input("De novo? [SIM/NAO] ").upper().strip()
    if continuar not in ["SIM", 'S']:
        break
