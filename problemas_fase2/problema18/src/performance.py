import random
import timeit

from main import maior_menor_indice, maior_menor_indice2


def gerar_lista_repetida_ordenada(tamanho, valor_min=0, valor_max=100):
    lista = [random.randint(valor_min, valor_max) for _ in range(tamanho)]
    lista.sort()
    return lista


def medir(func, number=10_000, repeat=5):
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    medio = sum(tempos) / len(tempos)
    return melhor, medio, tempos


def benchmark():
    random.seed(42)

    lista = gerar_lista_repetida_ordenada(100_000, 0, 500)

    # escolhe alvo garantidamente presente
    alvo = lista[len(lista) // 2]

    algoritmos = [
        ("busca_linear_indices", maior_menor_indice, "O(n)", "geral"),
        ("busca_binaria_dupla", maior_menor_indice2, "O(log n)", "lista ordenada"),
    ]

    resultados = []

    for nome, func, big_o, obs in algoritmos:
        runner = lambda f=func: f(lista, alvo)

        melhor, medio, tempos = medir(runner, number=5_000, repeat=5)

        resultados.append({
            "nome": nome,
            "big_o": big_o,
            "observacao": obs,
            "melhor": melhor,
            "medio": medio,
            "tempo_por_chamada": melhor / 5_000,
            "tempos": tempos,
        })

    resultados.sort(key=lambda x: x["melhor"])

    print(f"Tamanho da lista: {len(lista):,}")
    print(f"Alvo escolhido: {alvo}")
    print()

    print(
        f"{'Algoritmo':22} "
        f"{'Big-O':10} "
        f"{'Observação':16} "
        f"{'Melhor(s)':>12} "
        f"{'Médio(s)':>12} "
        f"{'Por chamada(s)':>16}"
    )
    print("-" * 95)

    for r in resultados:
        print(
            f"{r['nome']:22} "
            f"{r['big_o']:10} "
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
