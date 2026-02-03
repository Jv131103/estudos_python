import threading
import time


def cpu_bound(n):
    s = 0
    for i in range(n):
        s += i * i
    return s


def rodar_1_thread(n):
    t0 = time.perf_counter()
    cpu_bound(n)
    return time.perf_counter() - t0


def rodar_2_threads(n):
    t0 = time.perf_counter()
    t1 = threading.Thread(target=cpu_bound, args=(n,))
    t2 = threading.Thread(target=cpu_bound, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return time.perf_counter() - t0


N = 30_000_00  # ajuste se quiser (3 milhões)
print("1 thread:", rodar_1_thread(N))
print("2 threads:", rodar_2_threads(N))
