import random
import timeit
import tracemalloc

from main import Pilha


def medir(func):
    tracemalloc.start()

    tempo = timeit.timeit(func, number=1)

    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    memoria_kb = pico / 1024

    return tempo, memoria_kb


def caso_bom(n):
    def operacao():
        p = Pilha()

        for i in range(n):
            p.push(i)

        for _ in range(n):
            p.get_min()

    return medir(operacao)


def caso_medio(n):
    def operacao():
        p = Pilha()

        for i in range(n):

            if random.random() < 0.5:
                p.push(random.randint(0, n))

            else:
                if p.dados:
                    p.get_min()

    return medir(operacao)


def caso_ruim(n):
    def operacao():
        p = Pilha()

        for i in range(n):
            p.push(random.randint(0, n))

        for _ in range(n):
            p.pop()

    return medir(operacao)


def benchmark():

    tamanhos = {
        "POUCOS": 1_000,
        "MÉDIOS": 100_000,
        "MUITOS": 1_000_000
    }

    print("\n========== BENCHMARK PILHA MIN ==========\n")

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
