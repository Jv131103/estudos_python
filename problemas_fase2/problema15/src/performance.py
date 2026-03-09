import timeit

from main import espiral, espiral_direcoes, espiral_pop


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


def copia_profunda_matriz(matriz):
    return [linha[:] for linha in matriz]


def medir(func, number=1000, repeat=5):
    tempos = timeit.repeat(func, number=number, repeat=repeat)
    melhor = min(tempos)
    medio = sum(tempos) / len(tempos)
    return melhor, medio, tempos


def benchmark():
    matriz = gerar_matriz(200, 200)

    algoritmos = [
        ("espiral_limites", espiral, "O(n*m)", "O(1) extra"),
        ("espiral_direcoes", espiral_direcoes, "O(n*m)", "O(n*m) visitado"),
        ("espiral_pop", espiral_pop, "O(n*m) prático*", "modifica matriz"),
    ]

    resultados = []

    for nome, func, big_o, memoria in algoritmos:
        melhor, medio, tempos = medir(
            lambda f=func: f(copia_profunda_matriz(matriz)),
            number=300,
            repeat=5
        )

        resultados.append({
            "nome": nome,
            "big_o": big_o,
            "memoria": memoria,
            "melhor": melhor,
            "medio": medio,
            "tempo_por_chamada": melhor / 300,
            "tempos": tempos,
        })

    resultados.sort(key=lambda x: x["melhor"])

    print(
        f"{'Algoritmo':20} "
        f"{'Big-O':14} "
        f"{'Memória':18} "
        f"{'Melhor(s)':>12} "
        f"{'Médio(s)':>12} "
        f"{'Por chamada(s)':>16}"
    )
    print("-" * 100)

    for r in resultados:
        print(
            f"{r['nome']:20} "
            f"{r['big_o']:14} "
            f"{r['memoria']:18} "
            f"{r['melhor']:12.6f} "
            f"{r['medio']:12.6f} "
            f"{r['tempo_por_chamada']:16.10f}"
        )

    mais_rapido = resultados[0]["melhor"]

    print("\nSpeedup relativo ao mais rápido:")
    print("-" * 45)

    for r in resultados:
        speedup = r["melhor"] / mais_rapido
        print(f"{r['nome']:20} {speedup:10.2f}x")


if __name__ == "__main__":
    benchmark()
