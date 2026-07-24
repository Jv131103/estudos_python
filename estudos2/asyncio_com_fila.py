import asyncio

import aiohttp


# Produtor: gera URLs para buscar
async def produtor(fila, urls):
    for url in urls:
        await fila.put(url)
        print(f"📥 URL adicionada: {url}")
        await asyncio.sleep(0.2)


# Consumidor: pega URLs e faz requisição
async def consumidor(nome, fila):
    while True:
        url = await fila.get()  # espera ter algo na fila
        print(f"🔄 {nome} processando: {url}")

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"✅ {nome} concluiu {url} — status: {response.status}")

        fila.task_done()  # avisa que terminou


async def main():
    fila = asyncio.Queue()
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
        "https://httpbin.org/uuid",
        "https://httpbin.org/user-agent",
    ]

    # Sobe 2 consumidores que ficam esperando trabalho
    consumidores = [
        asyncio.create_task(consumidor("Worker A", fila)),
        asyncio.create_task(consumidor("Worker B", fila)),
    ]

    # Produtor alimenta a fila
    await produtor(fila, urls)

    # Espera todos os itens serem processados
    await fila.join()

    # Cancela os consumidores (que ficam em loop infinito)
    for c in consumidores:
        c.cancel()

asyncio.run(main())
