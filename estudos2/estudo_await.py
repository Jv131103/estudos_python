import asyncio


async def tarefa():
    print("A")
    await asyncio.sleep(1)  # Não bloqueia o programa
    print("B")


asyncio.run(tarefa())
