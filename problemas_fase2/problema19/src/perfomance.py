import timeit

from main import verificar, verificar2, verificar3, verificar4


def gerar_balanceada_aninhada(n):
    """
    Gera algo como:
    n=3 -> ([{{}}])
    Aqui vou usar padrão simples: '((...))'
    tamanho final = 2n
    """
    return "(" * n + ")" * n


def gerar_balanceada_blocos(n):
    """
    Gera algo como:
    ()()()()...
    tamanho final = 2n
    """
    return "()" * n


def benchmark(funcoes, gerador, tamanhos, repeat=5, number=100):
    print(f"\n=== Benchmark: {gerador.__name__} ===")

    for n in tamanhos:
        caso = gerador(n)
        print(f"\nTamanho da string: {len(caso)}")

        for func in funcoes:
            tempo = min(
                timeit.repeat(
                    lambda: func(caso),
                    repeat=repeat,
                    number=number
                )
            )
            print(f"{func.__name__:12} -> {tempo:.6f} s")


if __name__ == "__main__":
    funcoes = [verificar, verificar2, verificar3, verificar4]
    tamanhos = [10, 100, 1000, 3000, 5000]

    benchmark(funcoes, gerar_balanceada_blocos, tamanhos)
    benchmark(funcoes, gerar_balanceada_aninhada, tamanhos)
