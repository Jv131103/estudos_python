import timeit
import tracemalloc
from random import randint

from main import PriorityQueue

NUM_ELEMENTOS = 5000
REPETICOES = 5


def gerar_elementos():
    valor = chr(randint(65, 90))      # A-Z
    prioridade = randint(1, 3)        # 1 emergência, 2 urgente, 3 normal
    return valor, prioridade


def medir_tempo(func, repeticoes=REPETICOES):
    tempo = timeit.timeit(func, number=repeticoes)
    return tempo / repeticoes


def medir_memoria(func):
    tracemalloc.start()
    func()
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


def caso_push():
    fila = PriorityQueue()
    for _ in range(NUM_ELEMENTOS):
        fila.push(*gerar_elementos())


def caso_pop():
    fila = PriorityQueue()
    for _ in range(NUM_ELEMENTOS):
        fila.push(*gerar_elementos())

    for _ in range(NUM_ELEMENTOS):
        fila.pop()


def caso_misto():
    fila = PriorityQueue()

    for _ in range(NUM_ELEMENTOS):
        fila.push(*gerar_elementos())

    for _ in range(NUM_ELEMENTOS // 2):
        fila.pop()
        fila.push(*gerar_elementos())


def caso_completo():
    fila = PriorityQueue()

    for _ in range(NUM_ELEMENTOS):
        fila.push(*gerar_elementos())

    for _ in range(NUM_ELEMENTOS // 2):
        fila.pop()

    for _ in range(NUM_ELEMENTOS // 2):
        fila.push(*gerar_elementos())

    while fila.dados:
        fila.pop()


def benchmark():
    testes = {
        "push": caso_push,
        "pop": caso_pop,
        "misto": caso_misto,
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
