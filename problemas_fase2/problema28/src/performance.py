import timeit
import tracemalloc

from main import FilaCircular

NUM_ELEMENTOS = 100000
REPETICOES = 5


def medir_tempo(func, repeticoes=REPETICOES):
    tempo = timeit.timeit(func, number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func):
    tracemalloc.start()
    func()
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def caso_enqueue():
    fila = FilaCircular(NUM_ELEMENTOS)

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)


def caso_dequeue():
    fila = FilaCircular(NUM_ELEMENTOS)

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS):
        fila.dequeue()


def caso_misto():
    fila = FilaCircular(NUM_ELEMENTOS)

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for i in range(NUM_ELEMENTOS // 2):
        fila.dequeue()
        fila.enqueue(i)


def caso_circular():
    fila = FilaCircular(NUM_ELEMENTOS)

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for i in range(NUM_ELEMENTOS):
        fila.dequeue()
        fila.enqueue(i)


def benchmark():

    testes = {
        "enqueue": caso_enqueue,
        "dequeue": caso_dequeue,
        "misto": caso_misto,
        "circular": caso_circular
    }

    print(f"{'Caso':<15} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
    print("-" * 70)

    for nome, func in testes.items():
        tempo = medir_tempo(func)
        atual, pico = medir_memoria(func)

        print(
            f"{nome:<15} "
            f"{tempo:<15.6f} "
            f"{atual / 1024:<18.2f} "
            f"{pico / 1024:<15.2f}"
        )


if __name__ == "__main__":
    benchmark()
