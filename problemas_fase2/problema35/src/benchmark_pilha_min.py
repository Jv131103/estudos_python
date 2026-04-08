import gc
import statistics
import timeit
import tracemalloc

from pilha_ingenua import PilhaIngenua
from pilha_min import PilhaMin


def gerar_dados(n):
    return list(range(n, 0, -1))


def aquecer(classe_pilha, rodadas=200, tamanho=100):
    for _ in range(rodadas):
        pilha = classe_pilha()
        for i in range(tamanho):
            pilha.push(i)
        for _ in range(tamanho):
            pilha.pop()


def escolher_number(n, operacao):
    if operacao == "get_min":
        if n <= 100:
            return 5000
        if n <= 1000:
            return 1000
        if n <= 10000:
            return 100
        return 10

    if n <= 100:
        return 5000
    if n <= 1000:
        return 1000
    if n <= 10000:
        return 100
    return 10


def medir_tempo(func, repeat=7, number=100):
    gc.collect()
    gc.disable()
    try:
        tempos = timeit.repeat(func, repeat=repeat, number=number)
    finally:
        gc.enable()

    tempos_por_execucao = [tempo / number for tempo in tempos]

    return {
        "min": min(tempos_por_execucao),
        "mean": statistics.mean(tempos_por_execucao),
        "stdev": statistics.stdev(tempos_por_execucao) if len(tempos_por_execucao) > 1 else 0.0,
        "raw": tempos_por_execucao,
    }


def medir_memoria(func):
    gc.collect()
    tracemalloc.start()
    try:
        func()
        _, pico = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()

    return pico / 1024


def benchmark_push(classe_pilha, n):
    dados = gerar_dados(n)

    def executar():
        pilha = classe_pilha()
        for valor in dados:
            pilha.push(valor)

    number = escolher_number(n, "push")
    tempo_info = medir_tempo(executar, repeat=7, number=number)
    memoria_kb = medir_memoria(executar)

    return tempo_info, memoria_kb


def benchmark_pop(classe_pilha, n):
    dados = gerar_dados(n)

    def executar():
        pilha = classe_pilha()
        for valor in dados:
            pilha.push(valor)

        for _ in range(n):
            pilha.pop()

    number = escolher_number(n, "pop")
    tempo_info = medir_tempo(executar, repeat=7, number=number)
    memoria_kb = medir_memoria(executar)

    return tempo_info, memoria_kb


def benchmark_get_min(classe_pilha, n):
    dados = gerar_dados(n)

    # prepara a pilha fora da medição para isolar melhor o get_min
    pilha = classe_pilha()
    for valor in dados:
        pilha.push(valor)

    repeticoes_get_min = min(n, 1000)

    def executar():
        for _ in range(repeticoes_get_min):
            pilha.get_min()

    number = escolher_number(n, "get_min")
    tempo_info = medir_tempo(executar, repeat=7, number=number)
    memoria_kb = medir_memoria(executar)

    return tempo_info, memoria_kb, repeticoes_get_min


def imprimir_linha(n, tempo_info, memoria_kb, extra=""):
    print(
        f"N={n:<6} | "
        f"min={tempo_info['min']:.8f}s | "
        f"média={tempo_info['mean']:.8f}s | "
        f"desvio={tempo_info['stdev']:.8f}s | "
        f"memória={memoria_kb:.2f} KB"
        f"{extra}"
    )


def executar_benchmarks():
    tamanhos = [10, 100, 1000, 10000, 100000]
    classes = [
        ("PilhaIngenua", PilhaIngenua),
        ("PilhaMin", PilhaMin),
    ]

    for nome, classe in classes:
        aquecer(classe)

        print(f"\n{'=' * 90}")
        print(f"Benchmark: {nome}")
        print(f"{'=' * 90}")

        print("\n[ PUSH ]")
        for n in tamanhos:
            tempo_info, memoria_kb = benchmark_push(classe, n)
            imprimir_linha(n, tempo_info, memoria_kb)

        print("\n[ POP ]")
        for n in tamanhos:
            tempo_info, memoria_kb = benchmark_pop(classe, n)
            imprimir_linha(n, tempo_info, memoria_kb)

        print("\n[ GET_MIN ]")
        for n in tamanhos:
            tempo_info, memoria_kb, repeticoes = benchmark_get_min(classe, n)
            imprimir_linha(n, tempo_info, memoria_kb, extra=f" | chamadas_get_min={repeticoes}")


if __name__ == "__main__":
    executar_benchmarks()
