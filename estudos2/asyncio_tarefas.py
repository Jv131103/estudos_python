import asyncio
import time


async def tarefa(function, *args, **kwargs):
    print(f"Executando {function.__name__}")
    inicio = time.perf_counter()
    await function(*args, **kwargs)
    fim = time.perf_counter()
    print(f"{function.__name__} terminou após {fim - inicio:.1f}s")


async def baixar_arquivo(nome_arquivo):
    print(f"Baixando arquivo {nome_arquivo}...")
    await asyncio.sleep(3)
    print("Arquivo baixado!")


async def consultar_api(url, method):
    print(f"Realizando consulta na url: {url} | Método: {method}")
    await asyncio.sleep(2)
    print("API Acessada")


async def consultar_banco():
    print("Lendo banco de dados...")
    await asyncio.sleep(1)
    print("API Acessada")


async def main():
    inicio = time.perf_counter()
    await asyncio.gather(
        tarefa(baixar_arquivo, "Gta San Andreas"),
        tarefa(consultar_api, "https://api.com", "GET"),
        tarefa(consultar_banco),
    )
    fim = time.perf_counter()
    print(f"\nTempo total: {fim - inicio:.1f}s")


asyncio.run(main())
