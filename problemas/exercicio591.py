"""
Faça um programa que:

    Crie uma função async def esperar(n)

    Dentro dela:

        espere n segundos (asyncio.sleep)

    Crie 3 tarefas com tempos diferentes

    Execute todas juntas com asyncio.gather

    Observe a ordem das mensagens

DICAS

    Use print antes e depois do await

    A ordem de término não é a mesma de criação

Isso é concorrência cooperativa

Objetivo:

    entender execução concorrente sem threads.
"""

import asyncio


async def esperar(n):
    try:
        print(f"Esperando {n} segundos")
        await asyncio.sleep(n)
        print("Sucesso!")
        return True
    except Exception as e:
        print(f"Erro de execução da Thread: {e}")
        return False


async def main():
    tar1, tar2, tar3 = await asyncio.gather(
        esperar(2),
        esperar(4),
        esperar(6)
    )
    print(tar1, tar2, tar3)


asyncio.run(main())
