import timeit
import tracemalloc

from main import Fila

NUM_ELEMENTOS = 50000
REPETICOES = 5


def medir_tempo(func):
    return timeit.timeit(func, number=REPETICOES) / REPETICOES


def medir_memoria(func):
    tracemalloc.start()
    func()
    atual, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return atual, pico


# 1) Melhor caso: só inserção
def melhor_caso():
    fila = Fila()
    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)


# 2) Pior caso: muitas remoções do início
def pior_caso():
    fila = Fila()
    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS):
        fila.dequeue()


# 3) Caso médio 1: metade entra, metade sai, alternado
def medio1():
    fila = Fila()
    for i in range(NUM_ELEMENTOS):
        fila.enqueue(i)

    for i in range(NUM_ELEMENTOS // 2):
        fila.dequeue()
        fila.enqueue(i)


# 4) Caso médio 2: crescimento parcial e redução parcial
def medio2():
    fila = Fila()

    for i in range(NUM_ELEMENTOS // 2):
        fila.enqueue(i)

    for _ in range(NUM_ELEMENTOS // 4):
        fila.dequeue()

    for i in range(NUM_ELEMENTOS // 2, NUM_ELEMENTOS):
        fila.enqueue(i)


tests = {
    "melhor_caso": melhor_caso,
    "pior_caso": pior_caso,
    "medio1": medio1,
    "medio2": medio2
}

print(f"{'Caso':<15} {'Tempo (s)':<15} {'Mem atual (KB)':<18} {'Pico (KB)':<15}")
print("-" * 65)

for nome, func in tests.items():
    tempo = medir_tempo(func)
    atual, pico = medir_memoria(func)
    print(f"{nome:<15} {tempo:<15.6f} {atual / 1024:<18.2f} {pico / 1024:<15.2f}")
