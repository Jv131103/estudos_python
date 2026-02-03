import threading

contador = 0


def inc():
    global contador
    for _ in range(100_000):
        contador += 1  # não é atômico


threads = [threading.Thread(target=inc) for _ in range(2)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print(contador)  # às vezes < 200000
