import timeit

from main import (encontrar_ponto_rotacao, encontrar_ponto_rotacao_binaria,
                  encontrar_ponto_rotacao_linear,
                  encontrar_ponto_rotacao_min_manual,
                  encontrar_ponto_rotacao_vizinhos)


def gerar_lista_rotacionada(n: int, k: int) -> list[int]:
    if n <= 0:
        raise ValueError("n deve ser maior que 0")

    lista = list(range(n))
    k %= n
    return lista[-k:] + lista[:-k]


def medir(func, number=10_000, repeat=5) -> tuple[float, list[float]]:
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    return melhor, tempos


def benchmark():
    algoritmos = [
        ("binary_search_pivot", encontrar_ponto_rotacao, "O(log n)"),
        ("binary_search_right", encontrar_ponto_rotacao_binaria, "O(log n)"),
        ("binary_search_neighbors", encontrar_ponto_rotacao_vizinhos, "O(log n)"),
        ("linear_break_detection", encontrar_ponto_rotacao_linear, "O(n)"),
        ("linear_minimum_scan", encontrar_ponto_rotacao_min_manual, "O(n)"),
    ]

    tamanhos = [1_000, 10_000, 100_000]

    for n in tamanhos:
        k = n // 3
        lista = gerar_lista_rotacionada(n, k)

        # ajusta repetições para não ficar pesado demais
        if n <= 1_000:
            number = 20_000
        elif n <= 10_000:
            number = 10_000
        else:
            number = 2_000

        resultados = []

        print(f"\n{'=' * 80}")
        print(f"BENCHMARK | tamanho={n:,} | rotação={k:,} | repetições={number:,}")
        print(f"{'=' * 80}")

        for nome, func, big_o in algoritmos:
            melhor, tempos = medir(lambda f=func: f(lista), number=number, repeat=5)
            medio_por_chamada = melhor / number
            resultados.append((nome, big_o, melhor, medio_por_chamada, tempos))

        resultados.sort(key=lambda x: x[2])

        print(f"{'Algoritmo':28} {'Big-O':10} {'Melhor tempo':15} {'Tempo/chamada'}")
        print("-" * 80)

        for nome, big_o, melhor, medio_por_chamada, _ in resultados:
            print(
                f"{nome:28} {big_o:10} "
                f"{melhor:15.6f} s "
                f"{medio_por_chamada:.10f} s"
            )

        mais_rapido = resultados[0][2]

        print("\nSpeedup relativo ao mais rápido:")
        print("-" * 80)
        for nome, _, melhor, _, _ in resultados:
            speedup = melhor / mais_rapido
            print(f"{nome:28} {speedup:10.2f}x")


if __name__ == "__main__":
    benchmark()
