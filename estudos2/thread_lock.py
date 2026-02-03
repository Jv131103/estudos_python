from threading import Lock, Thread

lock = Lock()
contador = 0


def inc():
    global contador
    for _ in range(10000):
        with lock:
            contador += 1


threads = [Thread(target=inc) for _ in range(2)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(contador)
