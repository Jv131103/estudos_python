import timeit

from main import busca1, busca2, busca3, busca4, busca5, busca6, busca7, busca8


def medir(func, number=10_000, repeat=5):
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    medio = sum(tempos) / len(tempos)
    return melhor, medio, tempos


def benchmark():
    lista = list(range(900))
    alvo = 899  # pior caso: elemento no final

    algoritmos = [
        ("busca1_for_indices", busca1, "O(n)", "iterativa"),
        ("busca2_for_valores", busca2, "O(n)", "iterativa"),
        ("busca3_enumerate", busca3, "O(n)", "iterativa"),
        ("busca4_while", busca4, "O(n)", "iterativa"),
        ("busca5_sentinela", busca5, "O(n)", "modifica lista"),
        ("busca6_index", busca6, "O(n)", "C interno"),
        ("busca7_list_comp", busca7, "O(n)", "cria lista"),
        ("busca8_recursiva", busca8, "O(n)", "pilha recursiva"),
    ]

    resultados = []

    for nome, func, big_o, obs in algoritmos:
        if nome == "busca5_sentinela":
            runner = lambda f=func: f(lista.copy(), alvo)
        else:
            runner = lambda f=func: f(lista, alvo)

        melhor, medio, tempos = medir(runner, number=1000, repeat=5)

        resultados.append({
            "nome": nome,
            "big_o": big_o,
            "observacao": obs,
            "melhor": melhor,
            "medio": medio,
            "tempo_por_chamada": melhor / 1000,
            "tempos": tempos,
        })

    resultados.sort(key=lambda x: x["melhor"])

    print(
        f"{'Algoritmo':22} "
        f"{'Big-O':8} "
        f"{'Observação':16} "
        f"{'Melhor(s)':>12} "
        f"{'Médio(s)':>12} "
        f"{'Por chamada(s)':>16}"
    )
    print("-" * 95)

    for r in resultados:
        print(
            f"{r['nome']:22} "
            f"{r['big_o']:8} "
            f"{r['observacao']:16} "
            f"{r['melhor']:12.6f} "
            f"{r['medio']:12.6f} "
            f"{r['tempo_por_chamada']:16.10f}"
        )

    mais_rapido = resultados[0]["melhor"]

    print("\nSpeedup relativo ao mais rápido:")
    print("-" * 45)
    for r in resultados:
        speedup = r["melhor"] / mais_rapido
        print(f"{r['nome']:22} {speedup:10.2f}x")


if __name__ == "__main__":
    benchmark()
