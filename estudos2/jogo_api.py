import requests


def jogo():
    url = "https://opentdb.com/api.php?amount=5&type=boolean"
    response = requests.get(url)
    response.raise_for_status()

    if not response.ok:
        print("Acesso API não encontrado")
        print(f"Retorno: {response.status_code}")
        print(f"Retorno (texto): {response.text}")
        return

    dados = response.json()

    acertos = 0
    for idx, valor in enumerate(dados['results'], start=1):
        while True:
            resp = input(f"{idx} = {valor['question']} (V or F): ").upper().strip()
            if resp not in ["V", "F"]:
                print("Digite apenas V ou F")
                continue
            break

        resp = 'True' if resp == "V" else 'False'
        saida = valor['correct_answer']

        if resp == saida:
            print("Acertou")
            acertos += 1
        else:
            print("Errou")
        print()

    print(f"Você acertou {acertos} de 5!")


jogo()
