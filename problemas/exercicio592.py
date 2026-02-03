"""
Faça um programa que:

    Crie um gerador assíncrono

    Ele deve:

        produzir números de 1 a 5

        esperar 0.5 segundo entre cada número

    Consuma os valores com async for

DICAS

    Use async def + yield

    Use await asyncio.sleep

    Pense como um “fluxo de dados”

Objetivo:

    entender yield + await juntos.
"""

import asyncio


async def cont(n, delay=3):
    for i in range(n):
        await asyncio.sleep(delay)
        yield i


async def main():
    dados = 10
    async for x in cont(dados, delay=1):
        print(x)


asyncio.run(main())
