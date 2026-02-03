import asyncio


async def stream():
    for i in range(3):
        await asyncio.sleep(0.2)
        yield i


async def main():
    async for x in stream():
        print(x)

asyncio.run(main())
