import timeit

from main import busca_binaria, busca_binaria_recursiva


def medir(func, number=10_000, repeat=5):
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    medio = sum(tempos) / len(tempos)
    return melhor, medio, tempos


def benchmark():
    lista = list(range(10_001))

    cenarios = {
        "melhor_caso": 5000,     # cai no meio logo de início
        "caso_inicio": 0,        # vai caminhando para a esquerda
        "caso_final": 10_000,    # vai caminhando para a direita
        "pior_caso": 10_001,     # não existe na lista
    }

    algoritmos = [
        ("busca_binaria_iterativa", busca_binaria, "O(log n)", "iterativa"),
        ("busca_binaria_recursiva", busca_binaria_recursiva, "O(log n)", "recursiva"),
    ]

    for nome_cenario, alvo in cenarios.items():
        print(f"\n{'=' * 90}")
        print(f"CENÁRIO: {nome_cenario} | alvo={alvo}")
        print(f"{'=' * 90}")

        resultados = []

        for nome_algoritmo, func, big_o, tipo in algoritmos:
            runner = lambda f=func, a=alvo: f(lista, a)

            melhor, medio, tempos = medir(runner, number=10_000, repeat=5)

            resultados.append({
                "nome": nome_algoritmo,
                "big_o": big_o,
                "tipo": tipo,
                "melhor": melhor,
                "medio": medio,
                "tempo_por_chamada": melhor / 10_000,
                "tempos": tempos,
            })

        resultados.sort(key=lambda x: x["melhor"])

        print(
            f"{'Algoritmo':28} "
            f"{'Big-O':10} "
            f"{'Tipo':12} "
            f"{'Melhor(s)':>12} "
            f"{'Médio(s)':>12} "
            f"{'Por chamada(s)':>16}"
        )
        print("-" * 90)

        for r in resultados:
            print(
                f"{r['nome']:28} "
                f"{r['big_o']:10} "
                f"{r['tipo']:12} "
                f"{r['melhor']:12.6f} "
                f"{r['medio']:12.6f} "
                f"{r['tempo_por_chamada']:16.10f}"
            )

        mais_rapido = resultados[0]["melhor"]

        print("\nSpeedup relativo ao mais rápido:")
        print("-" * 50)

        for r in resultados:
            speedup = r["melhor"] / mais_rapido
            print(f"{r['nome']:28} {speedup:10.2f}x")


if __name__ == "__main__":
    benchmark()
