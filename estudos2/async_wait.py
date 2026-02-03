import asyncio


async def job(i, t):
    await asyncio.sleep(t)
    return i


async def main():
    """
    WAIT quer controle (done/pending/timeout/first)
    """
    tasks = {
        asyncio.create_task(job(1, 1.0)),
        asyncio.create_task(job(2, 0.2))
    }

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for d in done:
        print("terminou:", await d)

    for p in pending:
        p.cancel()


asyncio.run(main())
