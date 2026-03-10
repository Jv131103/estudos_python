import random
import string
import timeit

from main import inverter_com_classe, inverter_lista_direto


def gerar_string(n):
    return "".join(random.choice(string.ascii_letters) for _ in range(n))


def benchmark(funcoes, tamanhos, repeat=5, number=100):

    print("\n=== Benchmark inversão de string ===")

    for n in tamanhos:

        s = gerar_string(n)

        print(f"\nTamanho da string: {n}")

        for func in funcoes:

            tempo = min(
                timeit.repeat(
                    lambda: func(s),
                    repeat=repeat,
                    number=number
                )
            )

            print(f"{func.__name__:22} -> {tempo:.6f} s")


if __name__ == "__main__":

    funcoes = [inverter_com_classe, inverter_lista_direto]

    tamanhos = [10, 100, 1000, 5000, 10000]

    benchmark(funcoes, tamanhos)
