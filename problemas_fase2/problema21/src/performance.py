import timeit

from main import avaliar_postfix, avaliar_prefix


def gerar_postfix_soma(n):
    """
    Gera expressão postfix equivalente a:
    1 + 1 + 1 + ... + 1
    com n operandos.
    Ex.: n=4 -> '1 1 + 1 + 1 +'
    """
    if n < 2:
        return "1"

    tokens = ["1", "1", "+"]
    for _ in range(n - 2):
        tokens.append("1")
        tokens.append("+")

    return " ".join(tokens)


def gerar_prefix_soma(n):
    """
    Gera expressão prefix equivalente a:
    1 + 1 + 1 + ... + 1
    com n operandos.
    Ex.: n=4 -> '+ + + 1 1 1 1'
    """
    if n < 2:
        return "1"

    operadores = ["+"] * (n - 1)
    operandos = ["1"] * n
    return " ".join(operadores + operandos)


def validar():
    tamanhos_teste = [2, 3, 5, 10]

    print("=== Validação ===")
    for n in tamanhos_teste:
        expr_post = gerar_postfix_soma(n)
        expr_pre = gerar_prefix_soma(n)

        r1 = avaliar_postfix(expr_post)
        r2 = avaliar_prefix(expr_pre)

        print(f"n={n:2} | postfix={r1} | prefix={r2}")


def benchmark(funcoes, geradores, tamanhos, repeat=5, number=1000):
    print("\n=== Benchmark avaliadores de expressão ===")

    for n in tamanhos:
        print(f"\nQuantidade de operandos: {n}")

        for nome, func in funcoes.items():
            expr = geradores[nome](n)

            tempo = min(
                timeit.repeat(
                    lambda: func(expr),
                    repeat=repeat,
                    number=number
                )
            )

            print(f"{nome:18} -> {tempo:.6f} s")


def benchmark_crescimento(funcoes, geradores, tamanhos, repeat=5, number=1000):
    print("\n=== Crescimento ===")

    for nome, func in funcoes.items():
        print(f"\n--- {nome} ---")
        tempos = []

        for n in tamanhos:
            expr = geradores[nome](n)
            tempo = min(
                timeit.repeat(
                    lambda: func(expr),
                    repeat=repeat,
                    number=number
                )
            )
            tempos.append((n, tempo))

        for i, (n, tempo) in enumerate(tempos):
            if i == 0:
                print(f"n={n:6} -> {tempo:.6f} s")
            else:
                n_ant, tempo_ant = tempos[i - 1]
                razao_n = n / n_ant
                razao_tempo = tempo / tempo_ant if tempo_ant else 0
                print(
                    f"n={n:6} -> {tempo:.6f} s | "
                    f"x tamanho={razao_n:.2f} | "
                    f"x tempo={razao_tempo:.2f}"
                )


if __name__ == "__main__":
    validar()

    funcoes = {
        "avaliar_postfix": avaliar_postfix,
        "avaliar_prefix": avaliar_prefix
    }

    geradores = {
        "avaliar_postfix": gerar_postfix_soma,
        "avaliar_prefix": gerar_prefix_soma
    }

    tamanhos = [10, 100, 1000, 5000, 10000]

    benchmark(funcoes, geradores, tamanhos, repeat=5, number=1000)
    benchmark_crescimento(funcoes, geradores, tamanhos, repeat=5, number=1000)
