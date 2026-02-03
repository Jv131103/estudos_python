import asyncio


async def job(i):
    await asyncio.sleep(0.2)
    return i * 2


async def main():
    """GATHER PEGA TUDO"""
    resultados = await asyncio.gather(job(1), job(2), job(3))
    print(resultados)  # [2, 4, 6]

asyncio.run(main())
