import os

import requests
from dotenv import load_dotenv

load_dotenv()


def buscar_pais(nome: str) -> None:
    if not isinstance(nome, str):
        raise ValueError("Nome do país precisa ser do tipo string")

    nome = nome.strip().lower()

    url = f"https://api.restcountries.com/countries/v5?q={nome}"

    headers = {
        "Authorization": os.getenv("BEARER_TK", "")
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    if not response.ok:
        print(f"País {nome} não encontrado")
        print(f"Retorno: {response.status_code}")
        print(f"Retorno (texto): {response.text}")
        return

    dados = response.json()
    print(f"País: {nome.title()}")
    print(f"Capital: {dados['data']['objects'][0]['capitals'][0]['name']}")
    print(f"População: {dados['data']['objects'][0]['population']}")
    print(f"Região: {dados['data']['objects'][0]['region']}")


buscar_pais("Brazil")
