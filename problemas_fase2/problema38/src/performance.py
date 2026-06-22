import sys
import time
import tracemalloc

from look_say import look_and_say1, look_and_say2

sys.setrecursionlimit(10000)


# ── Gerar entradas de teste iterando a sequência ───────────────────────────────

def gerar_sequencia(n):
    s = "1"
    for _ in range(n):
        s = look_and_say1(s)
    return s


entradas = {
    "pequena (len~6)": gerar_sequencia(5),
    "média  (len~26)": gerar_sequencia(10),
    "grande (len~102)": gerar_sequencia(15),
    "enorme (len~226)": gerar_sequencia(18),
}

funcoes = [
    ("Loop manual", look_and_say1),
    ("Recursão", look_and_say2),
]

REPETICOES = 1000

# ── Benchmark ──────────────────────────────────────────────────────────────────

print(f"\n{'Função':<16} {'Entrada':<24} {'Tempo(ms)':>10} {'Mem pico(KB)':>13} {'Mem líq(KB)':>12}")
print("-" * 78)

for nome_fn, fn in funcoes:
    for nome_entrada, entrada in entradas.items():

        if fn == look_and_say2 and len(entrada) > 500:
            print(f"{nome_fn:<16} {nome_entrada:<24} {'SKIP (estouro de pilha)':>36}")
            continue

        reps = REPETICOES if len(entrada) < 1000 else 100

        # Tempo
        start = time.perf_counter()
        for _ in range(reps):
            fn(entrada)
        elapsed = (time.perf_counter() - start) / reps * 1000

        # Memória
        tracemalloc.start()
        fn(entrada)
        atual, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(
            f"{nome_fn:<16} {nome_entrada:<24}"
            f" {elapsed:>10.4f}"
            f" {pico / 1024:>13.2f}"
            f" {atual / 1024:>12.2f}"
        )

print()
print("Tamanhos reais das entradas:")
for nome, entrada in entradas.items():
    print(f"  {nome}: len={len(entrada)}")
