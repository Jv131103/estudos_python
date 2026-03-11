import timeit
import tracemalloc

from main import (gerar_binario_fila_lista_direta, gerar_binarios_bin,
                  gerar_binarios_fila, gerar_binarios_fstring,
                  gerar_binarios_manual, gerar_binarios_recursivo)


def medir_tempo(func, n, repeticoes=5):
    tempo = timeit.timeit(lambda: func(n), number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func, n):
    tracemalloc.start()
    func(n)
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def benchmark(n=1000):
    testes = {
        "fila_classe": gerar_binarios_fila,
        "fila_lista_direta": gerar_binario_fila_lista_direta,
        "manual": gerar_binarios_manual,
        "bin": gerar_binarios_bin,
        "fstring": gerar_binarios_fstring,
        "recursivo": gerar_binarios_recursivo,
    }

    print(f"{'Algoritmo':<20} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
    print("-" * 75)

    for nome, func in testes.items():
        tempo = medir_tempo(func, n)
        atual, pico = medir_memoria(func, n)

        print(f"{nome:<20} {tempo:<15.6f} {atual / 1024:<18.2f} {pico / 1024:<15.2f}")


if __name__ == "__main__":
    benchmark(5000)
