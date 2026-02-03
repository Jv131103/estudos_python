"""
Crie um script que:

    mostre a data atual no formato DD/MM/YYYY

    mostre a hora atual no formato HH:MM
"""

import datetime

hoje = datetime.datetime.today()

data_de_hoje = hoje.strftime("%d/%m/%Y")
print(data_de_hoje)

hora_atual = hoje.strftime("%H:%M")
print(hora_atual)
