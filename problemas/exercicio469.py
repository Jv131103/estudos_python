"""
Leia um horário no formato:

    HH:MM:SS


Mostre:

    horas

    minutos

    segundos (todos como int)

Use split e conversão.
"""


def retornar_tempo(horario_str):
    partes = horario_str.split(":")

    if len(partes) != 3:
        print("Formato inválido, precisa estar no formato HH:MM:SS")
        return

    try:
        hora = int(partes[0])
        minuto = int(partes[1])
        segundo = int(partes[2])
    except ValueError:
        print("Formato inválido: valores precisam ser números")
        return

    if not (0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59):
        print("Formato inválido")
        print("Horas: 0–23")
        print("Minutos/Segundos: 0–59")
        return

    print(f"Hora: {hora}")
    print(f"Minuto: {minuto}")
    print(f"Segundo: {segundo}")


retornar_tempo("02:45:12")
