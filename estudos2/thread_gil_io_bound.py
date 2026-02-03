import threading
import time


def io_bound():
    time.sleep(1)  # simula I/O (rede/disco)


def rodar_sequencial():
    t0 = time.perf_counter()
    io_bound()
    io_bound()
    return time.perf_counter() - t0


def rodar_threads():
    t0 = time.perf_counter()
    t1 = threading.Thread(target=io_bound)
    t2 = threading.Thread(target=io_bound)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return time.perf_counter() - t0


print("sequencial:", rodar_sequencial())
print("threads:", rodar_threads())
