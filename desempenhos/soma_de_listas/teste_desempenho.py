import gc
import os
import platform
import statistics as stats
import time
import tracemalloc

from soma_div_recursiva import (soma_div_conquer, soma_recursiva,
                                soma_recursiva2)
from soma_estrutural import (soma_estrutural1, soma_estrutural2,
                             soma_estrutural3)
from soma_pythonico import soma_pythonico

FUNCS = [
    ("estrutural1", soma_estrutural1),
    ("estrutural2", soma_estrutural2),
    ("estrutural3", soma_estrutural3),
    ("pythonic", soma_pythonico),
    ("divide_and_conquer", soma_div_conquer),
    ("recursiva1", soma_recursiva),
    ("recursiva2", soma_recursiva2)
]


def get_rss_bytes_unix():
    """
    Pico de memória do processo (aprox.) no Linux/macOS via 'resource'.
    Em Windows, retorna None.
    """
    if os.name != "posix":
        return None
    try:
        import resource
        r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        # Linux: ru_maxrss vem em KB; macOS: vem em bytes
        if platform.system() == "Darwin":
            return int(r)
        return int(r) * 1024
    except Exception:
        return None


def bench(func, data, reps=30, warmup=5):
    # Warmup (compila caminhos, cache, etc.)
    for _ in range(warmup):
        func(data)

    # Para reduzir ruído de GC durante medida (opcional)
    gc.collect()
    gc_was_enabled = gc.isenabled()
    gc.disable()

    times_ns = []
    tracemalloc.start()
    peak_py_bytes = 0

    rss_before = get_rss_bytes_unix()

    try:
        for _ in range(reps):
            t0 = time.perf_counter_ns()
            # out = func(data)
            t1 = time.perf_counter_ns()
            times_ns.append(t1 - t0)

            # pico de memória (só alocações Python rastreadas)
            _, peak = tracemalloc.get_traced_memory()
            if peak > peak_py_bytes:
                peak_py_bytes = peak

        rss_after = get_rss_bytes_unix()
    finally:
        tracemalloc.stop()
        if gc_was_enabled:
            gc.enable()

    # Stats tempo
    mean_ns = int(stats.mean(times_ns))
    med_ns = int(stats.median(times_ns))
    min_ns = int(min(times_ns))
    max_ns = int(max(times_ns))
    stdev_ns = int(stats.pstdev(times_ns)) if len(times_ns) > 1 else 0

    # Delta RSS (aprox.) — cuidado: é “maxrss”, pode não diminuir
    rss_delta = None
    if rss_before is not None and rss_after is not None:
        rss_delta = rss_after - rss_before

    return {
        "mean_ns": mean_ns,
        "median_ns": med_ns,
        "min_ns": min_ns,
        "max_ns": max_ns,
        "stdev_ns": stdev_ns,
        "peak_py_bytes": peak_py_bytes,
        "rss_delta_bytes": rss_delta,
    }


def fmt_bytes(n):
    if n is None:
        return "N/A"
    for unit in ["B", "KB", "MB", "GB"]:
        if n < 1024:
            return f"{n:.1f}{unit}" if isinstance(n, float) else f"{n}{unit}"
        n = n / 1024
    return f"{n:.1f}TB"


def fmt_ns(ns):
    # converte para us/ms/s de forma legível
    if ns < 1_000:
        return f"{ns} ns"
    if ns < 1_000_000:
        return f"{ns / 1_000:.2f} µs"
    if ns < 1_000_000_000:
        return f"{ns / 1_000_000:.2f} ms"
    return f"{ns / 1_000_000_000:.3f} s"


def main():
    # Ajuste o tamanho do teste
    N = 500
    data = list(range(N))

    print(f"Python: {platform.python_version()} | OS: {platform.system()} {platform.release()}")
    print(f"Entrada: lista com {N:,} inteiros\n")

    # Confere se todas retornam o mesmo resultado (sanidade)
    resultados = {}
    for name, f in FUNCS:
        resultados[name] = f(data)

    if len(set(resultados.values())) != 1:
        print("⚠️ ALERTA: funções retornaram resultados diferentes!")
        for k, v in resultados.items():
            print(k, v)
        return

    print("✅ Todas retornaram o mesmo resultado.\n")

    # Rodar benchmark
    for name, f in FUNCS:
        r = bench(f, data, reps=30, warmup=5)
        print(f"== {name} ==")
        print(f"Tempo (média):   {fmt_ns(r['mean_ns'])}")
        print(f"Tempo (mediana): {fmt_ns(r['median_ns'])}")
        print(f"Tempo (min/max): {fmt_ns(r['min_ns'])} / {fmt_ns(r['max_ns'])}")
        print(f"Ruído (stdev):   {fmt_ns(r['stdev_ns'])}")
        print(f"Pico mem Python: {fmt_bytes(r['peak_py_bytes'])}")
        print(f"RSS delta proc.: {fmt_bytes(r['rss_delta_bytes'])}")
        print()


if __name__ == "__main__":
    main()
