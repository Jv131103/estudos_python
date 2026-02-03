"""
Faça um programa que:

    Use uma variável global contador

    Crie duas threads que:

        incrementam o contador várias vezes

    Observe o valor final

    Execute várias vezes

Depois:

    proteja o acesso ao contador

    compare os resultados

DICAS

    Comece com poucas iterações

    Depois aumente

    Use Lock para corrigir

Objetivo:

    ver um bug raro aparecer e aprender a corrigir.
"""

import threading
import time

contador = 0


def incrementar_varias_vezes(n):
    global contador
    for _ in range(n):
        temp = contador          # lê
        time.sleep(0)            # força troca de thread (aumenta chance do bug)
        contador = temp + 1      # escreve


def rodar_sem_lock(iteracoes=100_000):
    global contador
    contador = 0

    t1 = threading.Thread(target=incrementar_varias_vezes, args=(iteracoes,))
    t2 = threading.Thread(target=incrementar_varias_vezes, args=(iteracoes,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    esperado = 2 * iteracoes
    print(f"[SEM LOCK] contador={contador} | esperado={esperado} | perdeu={esperado - contador}")


# Rode várias vezes
for _ in range(5):
    rodar_sem_lock(50_000)
