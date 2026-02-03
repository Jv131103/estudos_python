import asyncio


async def job(i):
    await asyncio.sleep(0.2)
    return i * 2


async def main():
    t = asyncio.create_task(job(1))
    print("faz outra coisa")
    r = await t
    print(r)


asyncio.run(main())
