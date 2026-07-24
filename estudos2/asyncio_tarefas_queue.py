import asyncio


async def produtor(fila, tarefas):
    for tarefa in tarefas:
        await fila.put(tarefa)  # Adiciona na fila
        print(f"📥 tarefa adicionada: {tarefa}")
        await asyncio.sleep(0.2)


async def consumidor(nome, fila):
    while True:
        tarefa = await fila.get()  # espera ter algo na fila
        print(f"🔄 {nome} processando: {tarefa}")
        await asyncio.sleep(1)
        print(f"✅ {nome} concluiu {tarefa} — status: OK!")

        fila.task_done()


async def main():
    fila = asyncio.Queue()
    tarefas = [
        "Estudar programação",
        "Estudar Matemática",
        "Estudar Teologia Cristã e ler a bíblia",
        "Estudar Lógica",
        "Estudar Filosofia",
        "Estudar biologia",
        "Escrever meus poemas, orações e epístolas de exortação",
        "Se distrair com bons vídeos de história",
    ]

    # Sobe 2 consumidores que ficam esperando trabalho
    consumidores = [
        asyncio.create_task(consumidor("DE MANHÃ", fila)),
        asyncio.create_task(consumidor("DE TARDE", fila)),
        asyncio.create_task(consumidor("DE NOITE", fila)),
    ]

    # Produtor alimenta a fila
    await produtor(fila, tarefas)

    # Espera todos os itens serem processados
    await fila.join()

    # Cancela os consumidores (que ficam em loop infinito)
    for c in consumidores:
        c.cancel()

asyncio.run(main())
