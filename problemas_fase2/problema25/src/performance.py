import timeit
import tracemalloc

from main import FilaComPilha

NUM_ELEMENTOS = 50000
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
    fila = FilaComPilha()
    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)


def caso_dequeue():
    fila = FilaComPilha()
    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS):
        fila.dequeue()


def caso_misto():
    fila = FilaComPilha()

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for i in range(NUM_ELEMENTOS // 2):
        fila.dequeue()
        fila.enqueue(i)


def caso_peek():
    fila = FilaComPilha()

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS):
        fila.peek()


def caso_completo():
    fila = FilaComPilha()

    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS // 2):
        fila.dequeue()

    for i in range(NUM_ELEMENTOS, NUM_ELEMENTOS + NUM_ELEMENTOS // 2):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS // 2):
        fila.peek()

    while not fila.is_empty():
        fila.dequeue()


def benchmark():
    testes = {
        "enqueue": caso_enqueue,
        "dequeue": caso_dequeue,
        "misto": caso_misto,
        "peek": caso_peek,
        "completo": caso_completo,
    }

    print(f"{'Caso':<15} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
    print("-" * 70)

    for nome, func in testes.items():
        tempo = medir_tempo(func)
        atual, pico = medir_memoria(func)

        print(f"{nome:<15} {tempo:<15.6f} {atual / 1024:<18.2f} {pico / 1024:<15.2f}")


if __name__ == "__main__":
    benchmark()
