import requests


def previsao(cidade: str) -> None:
    if not isinstance(cidade, str):
        raise ValueError("Cidade precisa ser do tipo string")

    cidade = cidade.strip().lower()

    url = f"https://wttr.in/{cidade}?format=j1"
    response = requests.get(url)
    response.raise_for_status()

    if not response.ok:
        print(f"Cidade {cidade} não encontrado")
        print(f"Retorno: {response.status_code}")
        print(f"Retorno (texto): {response.text}")
        return

    dados = response.json()
    print(f"Cidade: {cidade}")
    print(f"Temperatura: {dados['current_condition'][0]['temp_C']} °C")
    print(f"Sensação: {dados['current_condition'][0]['FeelsLikeC']} °C")
    print(f"Clima: {dados['current_condition'][0]['weatherDesc'][0]['value']}")


previsao("São Paulo")
