"""
Faça um programa que:

    Crie uma função simples que:

        apenas imprima o nome da thread

    Crie 3 threads

    Execute todas

    Observe a ordem de saída

DICAS

    Use threading.current_thread().name

    Não use variáveis globais

    O foco é ver concorrência sem bug

Objetivo:

    entender threads como execução concorrente.
"""

import threading


def minha_funcao():
    print(threading.current_thread().name)


threads = []

for i in range(3):
    t = threading.Thread(target=minha_funcao)
    threads.append(t)
    t.start()


for t in threads:
    t.join()
