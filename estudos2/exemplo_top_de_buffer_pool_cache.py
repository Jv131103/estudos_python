import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Empty, Queue

# CACHE: guarda resultados já calculados
cache = {}

# BUFFER: fila de eventos
buffer = Queue()

# trava para proteger o cache
lock = threading.Lock()


def processar_evento(evento):
    usuario = evento["usuario"]

    # CACHE: evita recalcular dado repetido
    with lock:
        if usuario in cache:
            perfil = cache[usuario]
            print(f"[CACHE] Usuário {usuario} já estava em cache")
        else:
            print(f"[PROCESSANDO] Buscando perfil do usuário {usuario}")
            time.sleep(1)  # simula custo alto
            perfil = f"perfil_{usuario}"
            cache[usuario] = perfil

    print(f"[OK] Evento processado para {usuario}: {evento['acao']}")


def worker():
    while True:
        try:
            evento = buffer.get(timeout=2)
        except Empty:
            break

        processar_evento(evento)
        buffer.task_done()


# Simulando entrada de eventos -> BUFFER
eventos = [
    {"usuario": 1, "acao": "clique"},
    {"usuario": 2, "acao": "scroll"},
    {"usuario": 1, "acao": "busca"},
    {"usuario": 3, "acao": "clique"},
    {"usuario": 2, "acao": "compra"},
]

for e in eventos:
    buffer.put(e)

# POOL: reutiliza 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    for _ in range(3):
        executor.submit(worker)

buffer.join()
print("Fim do processamento")
