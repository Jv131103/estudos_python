"""
Verificar se os batimentos cardíacos por minuto se encontram na faixa
adequada. Para isso, você deve solicitar ao usuário que informe o seu
número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso, o
script deve verificar e exibir uma mensagem informando se os batimentos
do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada
ou ABAIXO da faixa adequada, de acordo com o site Tua Saúde
(<https://bit.ly/4aL3Mbo>):
"""


def bpm_is_ok(bpm, idade, unidade="anos"):
    if unidade == "dias":
        if 0 <= idade <= 28:
            faixa_min, faixa_max = 100, 205
            faixa = "0 a 28 dias"
        elif 28 < idade <= 365:
            faixa_min, faixa_max = 100, 180
            faixa = "28 dias a 1 ano"
        else:
            return print("Idade em dias inválida")

    elif unidade == "anos":
        if 1 <= idade < 3:
            faixa_min, faixa_max = 98, 140
            faixa = "1 a 3 anos"
        elif 3 <= idade < 5:
            faixa_min, faixa_max = 80, 120
            faixa = "3 a 5 anos"
        elif 5 <= idade < 12:
            faixa_min, faixa_max = 75, 118
            faixa = "5 a 12 anos"
        else:
            faixa_min, faixa_max = 60, 100
            faixa = "13+ anos"

    else:
        return print("Unidade inválida")

    if bpm < faixa_min:
        status = "ABAIXO da faixa"
    elif bpm > faixa_max:
        status = "ACIMA da faixa"
    else:
        status = "DENTRO da faixa"

    print(f"Faixa etária: {faixa}")
    print(f"Intervalo adequado: {faixa_min} a {faixa_max} bpm")
    print(f"Resultado: {status}")


bpm_is_ok(180, 28, "dias")
