def agenda_valida(consultas):
    if not consultas:
        return True

    fim_anterior = consultas[0][1]

    for inicio, fim in consultas[1:]:

        if inicio < fim_anterior:
            return False

        fim_anterior = fim

    return True


# 1 — Consultas sem conflitos
print(agenda_valida([(9, 10), (11, 12), (13, 14)]))
# True

# 2 — Consultas encostadas
print(agenda_valida([(9, 10), (10, 11), (11, 12)]))
# True

# 3 — Consultas sobrepostas
print(agenda_valida([(9, 11), (10, 12)]))
# False

# 4 — Conflito depois de uma consulta longa
print(agenda_valida([(8, 10), (11, 13), (12, 14)]))
# False

# 5 — Apenas uma consulta
print(agenda_valida([(14, 16)]))
# True

# 6 — Agenda vazia
print(agenda_valida([]))
# True

# 7 — Consultas com horários iguais de início
print(agenda_valida([(9, 11), (9, 10)]))
# False

# 8 — Muitas consultas consecutivas
print(agenda_valida([(8, 9), (9, 10), (10, 11), (11, 12)]))
# True
