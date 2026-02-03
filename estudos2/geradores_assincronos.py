import asyncio


async def gerar():
    for i in range(3):
        await asyncio.sleep(1)
        yield i


async def rodar():
    async for x in gerar():
        print(x)


asyncio.run(rodar())
