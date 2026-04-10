import time
from concurrent.futures import ThreadPoolExecutor


def tarefa(n):
    print(f"Executando {n}")
    time.sleep(1)
    return n * 2


with ThreadPoolExecutor(max_workers=3) as pool:
    resultados = list(pool.map(tarefa, range(5)))

print(resultados)
print(resultados)
