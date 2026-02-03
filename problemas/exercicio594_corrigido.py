import threading

contador = 0
lock = threading.Lock()


def incrementar_varias_vezes_com_lock(n):
    global contador
    for _ in range(n):
        with lock:
            contador += 1


def rodar_com_lock(iteracoes=100_000):
    global contador
    contador = 0

    t1 = threading.Thread(target=incrementar_varias_vezes_com_lock, args=(iteracoes,))
    t2 = threading.Thread(target=incrementar_varias_vezes_com_lock, args=(iteracoes,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    esperado = 2 * iteracoes
    print(f"[COM LOCK] contador={contador} | esperado={esperado} | ok={contador == esperado}")


for _ in range(5):
    rodar_com_lock(50_000)
