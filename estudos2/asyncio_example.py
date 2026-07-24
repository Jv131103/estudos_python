import asyncio


async def tarefa(nome, segundos):
    print(f"{nome} começou")
    await asyncio.sleep(segundos)  # simula espera (I/O, API, etc)
    print(f"{nome} terminou após {segundos}s")


async def main():
    await asyncio.gather(
        tarefa("A", 2),
        tarefa("B", 1),
        tarefa("C", 3),
    )

asyncio.run(main())
# A começou
# B começou
# C começou
# B terminou após 1s
# A terminou após 2s
# C terminou após 3s
# Total: ~3s (não 6s!)
