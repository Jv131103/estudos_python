import random
import timeit
import tracemalloc

from main import ArrayDinamico


def medir(func):

    tracemalloc.start()

    tempo = min(timeit.repeat(func, repeat=5, number=1))

    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memoria_kb = pico / 1024

    return tempo, memoria_kb


def caso_bom(n):

    def operacao():

        a = ArrayDinamico()

        for i in range(n):
            a.append(i)

        for i in range(n):
            a.get(i)

    return medir(operacao)


def caso_medio(n):

    ops = [random.random() < 0.5 for _ in range(n)]

    def operacao():

        a = ArrayDinamico()

        for i in range(n):

            if ops[i]:
                a.append(i)

            else:
                if a.size() > 0:
                    idx = i % a.size()
                    a.get(idx)

    return medir(operacao)


def caso_ruim(n):

    def operacao():

        a = ArrayDinamico()

        for i in range(n):
            a.append(i)

    return medir(operacao)


def benchmark():

    tamanhos = {
        "POUCOS": 1_000,
        "MÉDIOS": 100_000,
        "MUITOS": 1_000_000
    }

    print("\n========== BENCHMARK ARRAY DINÂMICO ==========\n")

    cabecalho = f"{'TAMANHO':<10} {'CASO':<10} {'TEMPO(s)':<12} {'MEMÓRIA(KB)':<12}"
    print(cabecalho)
    print("-" * len(cabecalho))

    for nome, n in tamanhos.items():

        tempo, mem = caso_bom(n)
        print(f"{nome:<10} {'BOM':<10} {tempo:<12.6f} {mem:<12.2f}")

        tempo, mem = caso_medio(n)
        print(f"{nome:<10} {'MÉDIO':<10} {tempo:<12.6f} {mem:<12.2f}")

        tempo, mem = caso_ruim(n)
        print(f"{nome:<10} {'RUIM':<10} {tempo:<12.6f} {mem:<12.2f}")

        print()


if __name__ == "__main__":
    benchmark()
