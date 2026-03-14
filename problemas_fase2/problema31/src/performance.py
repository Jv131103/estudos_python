import timeit
import tracemalloc

from main import (is_palinder_class_pilha, is_palinder_deque,
                  is_palinder_dois_ponteiros, is_palinder_list_pilha,
                  is_palinder_manual, is_palinder_recursicion,
                  is_palinder_reverse, is_palinder_slicing1,
                  is_palinder_slicing2)

REPETICOES = 5


def medir_tempo(func, valor, repeticoes=REPETICOES):
    tempo = timeit.timeit(lambda: func(valor), number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func, valor):
    tracemalloc.start()
    func(valor)
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def gerar_string_palindroma(tamanho):
    metade = "a" * (tamanho // 2)

    if tamanho % 2 == 0:
        return metade + metade[::-1]

    return metade + "b" + metade[::-1]


def gerar_string_nao_palindroma(tamanho):
    if tamanho < 2:
        return "ab"
    return "a" * (tamanho - 1) + "b"


def benchmark(valor, titulo):
    funcoes = {
        "deque": is_palinder_deque,
        "class_pilha": is_palinder_class_pilha,
        "list_pilha": is_palinder_list_pilha,
        "slicing1": is_palinder_slicing1,
        "slicing2": is_palinder_slicing2,
        "dois_ponteiros": is_palinder_dois_ponteiros,
        "manual": is_palinder_manual,
        "reverse": is_palinder_reverse,
        "recursao": is_palinder_recursicion,
    }

    print(f"\n=== {titulo} | tamanho={len(valor)} ===")
    print(f"{'Função':<18} {'Resultado':<10} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
    print("-" * 85)

    for nome, func in funcoes.items():
        try:
            resultado = func(valor)
            tempo = medir_tempo(func, valor)
            atual, pico = medir_memoria(func, valor)

            print(
                f"{nome:<18} "
                f"{str(resultado):<10} "
                f"{tempo:<15.6f} "
                f"{atual / 1024:<18.2f} "
                f"{pico / 1024:<15.2f}"
            )
        except RecursionError:
            print(
                f"{nome:<18} "
                f"{'ERRO':<10} "
                f"{'-':<15} "
                f"{'-':<18} "
                f"{'RecursionError':<15}"
            )


def main():
    tamanhos = [10, 100, 1000, 5000]

    for tamanho in tamanhos:
        valor_pal = gerar_string_palindroma(tamanho)
        valor_nao_pal = gerar_string_nao_palindroma(tamanho)

        benchmark(valor_pal, "PALÍNDROMO")
        benchmark(valor_nao_pal, "NÃO PALÍNDROMO")


if __name__ == "__main__":
    main()
