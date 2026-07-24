import asyncio
import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()


async def buscar_pais(nome):
    url = f"https://api.restcountries.com/countries/v5?q={nome}"
    async with aiohttp.ClientSession(
        headers={
            "User-Agent": "Mozilla/5.0",
            "Authorization": os.getenv('BEARER_TK', "")
        }
    ) as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    paises = ["brazil", "japan", "france", "germany", "canada"]

    # Cria uma lista de tarefas (coroutines)
    tarefas = [buscar_pais(pais) for pais in paises]

    # Dispara todas em paralelo e espera o resultado
    resultados = await asyncio.gather(*tarefas)

    print("Todos carregados com sucesso:")
    print()
    for resultado in resultados:
        dados = resultado  # retorna lista, pega o primeiro
        print(f"País: {dados['data']['objects'][0]['names']['common']}")
        print(f"Capital: {dados['data']['objects'][0]['capitals'][0]['name']}")
        print(f"População: {dados['data']['objects'][0]['population']:,}\n")


# Executa o loop de eventos
asyncio.run(main())
