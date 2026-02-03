"""
Faça um programa que:

    Tenha uma função async def tarefa()

    Dentro dela:

        use time.sleep(2)

    Crie duas tarefas com asyncio.gather

    Observe o tempo total de execução

Depois:

    substitua time.sleep por asyncio.sleep

    compare o tempo

DICAS

    Use time.time() para medir

    O objetivo é ver o erro acontecer

    Não se preocupe com performance real, só com o efeito

Objetivo:

    entender o que significa “bloquear o event loop”.
"""

import asyncio

# import time


async def tarefa(message, result, delay=3):
    # time.sleep(delay)
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    a, b = await asyncio.gather(
        tarefa('Calling API 1 ...', 100),
        tarefa('Calling API 2 ...', 200)
    )
    print(a, b)


asyncio.run(main())
