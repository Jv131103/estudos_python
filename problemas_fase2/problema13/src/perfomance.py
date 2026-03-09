import timeit

from main import somar_matriz, somar_matriz2, somar_matriz3, somar_matriz4


def gerar_matriz(linhas, colunas):
    valor = 1
    matriz = []

    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            linha.append(valor)
            valor += 1
        matriz.append(linha)

    return matriz


def medir(func, number=10_000, repeat=5):
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    medio = sum(tempos) / len(tempos)
    return melhor, medio, tempos


def benchmark():
    matriz = gerar_matriz(200, 200)

    algoritmos = [
        ("somar_matriz_manual_indices", somar_matriz, "O(linhas * colunas)"),
        ("somar_matriz_list_comp", somar_matriz2, "O(linhas * colunas)"),
        ("somar_matriz_loop_sum", somar_matriz3, "O(linhas * colunas)"),
        ("somar_matriz_formula_pa", somar_matriz4, "O(linhas) * se cada linha for PA"),
    ]

    resultados = []

    for nome, func, big_o in algoritmos:
        melhor, medio, tempos = medir(lambda f=func: f(matriz), number=1000, repeat=5)
        tempo_por_chamada = melhor / 1000

        resultados.append({
            "nome": nome,
            "big_o": big_o,
            "melhor": melhor,
            "medio": medio,
            "tempo_por_chamada": tempo_por_chamada,
            "tempos": tempos,
        })

    resultados.sort(key=lambda item: item["melhor"])

    print(f"{'Algoritmo':30} {'Big-O':28} {'Melhor(s)':>12} {'Médio(s)':>12} {'Por chamada(s)':>16}")
    print("-" * 105)

    for r in resultados:
        print(
            f"{r['nome']:30} "
            f"{r['big_o']:28} "
            f"{r['melhor']:12.6f} "
            f"{r['medio']:12.6f} "
            f"{r['tempo_por_chamada']:16.10f}"
        )

    mais_rapido = resultados[0]["melhor"]

    print("\nSpeedup relativo ao mais rápido:")
    print("-" * 50)
    for r in resultados:
        speedup = r["melhor"] / mais_rapido
        print(f"{r['nome']:30} {speedup:10.2f}x")


if __name__ == "__main__":
    benchmark()
