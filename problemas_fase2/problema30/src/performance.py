import timeit
import tracemalloc

from main import Deque

REPETICOES = 5
NUM_ELEMENTOS = 50000


def medir_tempo(func, repeticoes=REPETICOES):
    tempo = timeit.timeit(func, number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func):
    tracemalloc.start()
    func()
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def caso_append_right():
    dq = Deque()
    for i in range(NUM_ELEMENTOS):
        dq.append_right(i)


def caso_append_left():
    dq = Deque()
    for i in range(NUM_ELEMENTOS):
        dq.append_left(i)


def caso_pop_right():
    dq = Deque()
    for i in range(NUM_ELEMENTOS):
        dq.append_right(i)

    for _ in range(NUM_ELEMENTOS):
        dq.pop_right()


def caso_pop_left():
    dq = Deque()
    for i in range(NUM_ELEMENTOS):
        dq.append_right(i)

    for _ in range(NUM_ELEMENTOS):
        dq.pop_left()


def caso_misto():
    dq = Deque()

    for i in range(NUM_ELEMENTOS // 2):
        dq.append_right(i)

    for i in range(NUM_ELEMENTOS // 2):
        dq.append_left(i)

    for _ in range(NUM_ELEMENTOS // 4):
        dq.pop_right()
        dq.pop_left()

    for i in range(NUM_ELEMENTOS // 4):
        dq.append_right(i)
        dq.append_left(i)


def benchmark():
    testes = {
        "append_right": caso_append_right,
        "append_left": caso_append_left,
        "pop_right": caso_pop_right,
        "pop_left": caso_pop_left,
        "misto": caso_misto,
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
