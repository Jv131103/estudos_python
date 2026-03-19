import io
import random
import sys
import timeit
import tracemalloc

from main import modelo1, modelo2, modelo3, modelo4, modelo5, modelo6


def modelo_lixo(text):
    return text


def medir(func):
    supressor = io.StringIO()
    sys.stdout = supressor

    tracemalloc.start()
    tempo = min(timeit.repeat(func, repeat=5, number=1))
    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    sys.stdout = sys.__stdout__

    memoria_kb = pico / 1024
    return tempo, memoria_kb


def benchmark():
    # Aquecimento silencioso para evitar anomalia de memória na primeira execução
    supressor = io.StringIO()
    sys.stdout = supressor
    for modelo in [modelo1, modelo2, modelo3, modelo4, modelo5, modelo6]:
        modelo("aquecimento")
    sys.stdout = sys.__stdout__

    testes = {
        "Lixo, apenas, para limpar ruido": modelo_lixo,
        "modelo1 (dicionario performance O(n))": modelo1,
        "modelo2 (dicionario manual O(n))": modelo2,
        "modelo3 (loop manual O(n**2))": modelo3,
        "modelo4 (loop com count O(n**2))": modelo4,
        "modelo5 (dicionario com sorted O(n log n))": modelo5,
        "modelo6 (ordenado com contagem manual O(nlogn))": modelo6,
    }

    frase = " ".join(random.choices(["rato", "gato", "pato", "cachorro", "cobra"], k=1000))

    print(f"\n{'Modelo':<50} {'Tempo (ms)':>12} {'Memória (KB)':>14}")
    print("-" * 80)

    for nome, func in testes.items():
        tempo, memoria = medir(lambda f=func: f(frase))
        print(f"{nome:<50} {tempo * 1000:>11.3f}ms {memoria:>13.2f} KB")

    print("-" * 80)


if __name__ == "__main__":
    benchmark()
