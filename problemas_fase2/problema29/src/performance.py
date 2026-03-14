import timeit
import tracemalloc

from main import RingBuffer

NUM_ELEMENTOS = 100000
REPETICOES = 5
TAMANHO_BUFFER = 10000


def medir_tempo(func, repeticoes=REPETICOES):
    tempo = timeit.timeit(func, number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func):
    tracemalloc.start()
    func()
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def caso_adicionar():
    rb = RingBuffer(TAMANHO_BUFFER)

    for i in range(NUM_ELEMENTOS):
        rb.adicionar(f"log-{i}")


def caso_get_logs():
    rb = RingBuffer(TAMANHO_BUFFER)

    for i in range(NUM_ELEMENTOS):
        rb.adicionar(f"log-{i}")

    rb.get_logs()


def caso_snapshot():
    rb = RingBuffer(TAMANHO_BUFFER)

    for i in range(NUM_ELEMENTOS):
        rb.adicionar(f"log-{i}")

    rb.snapshot()


def caso_varios_snapshots():
    rb = RingBuffer(TAMANHO_BUFFER)

    for i in range(NUM_ELEMENTOS):
        rb.adicionar(f"log-{i}")

        if i % 1000 == 0:
            rb.snapshot()


def caso_misto():
    rb = RingBuffer(TAMANHO_BUFFER)

    for i in range(NUM_ELEMENTOS):
        rb.adicionar(f"log-{i}")

        if i % 500 == 0:
            rb.get_logs()

        if i % 1000 == 0:
            rb.snapshot()


def benchmark():
    testes = {
        "adicionar": caso_adicionar,
        "get_logs": caso_get_logs,
        "snapshot": caso_snapshot,
        "varios_snapshots": caso_varios_snapshots,
        "misto": caso_misto,
    }

    print(f"{'Caso':<20} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
    print("-" * 75)

    for nome, func in testes.items():
        tempo = medir_tempo(func)
        atual, pico = medir_memoria(func)

        print(
            f"{nome:<20} "
            f"{tempo:<15.6f} "
            f"{atual / 1024:<18.2f} "
            f"{pico / 1024:<15.2f}"
        )


if __name__ == "__main__":
    benchmark()
