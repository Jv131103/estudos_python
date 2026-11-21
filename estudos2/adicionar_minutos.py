def adicionar_minutos(hora, minuto, acrescimo):
    total_minutos = hora * 60 + minuto + acrescimo

    nova_hora = (total_minutos // 60) % 24
    novo_minuto = total_minutos % 60

    return f"{nova_hora:02d}:{novo_minuto:02d}"


print(adicionar_minutos(23, 50, 20))
print(adicionar_minutos(10, 5, 0))
print(adicionar_minutos(8, 45, 30))
print(adicionar_minutos(12, 59, 1))
print(adicionar_minutos(0, 0, 1440))
print(adicionar_minutos(23, 59, 2))
print(adicionar_minutos(22, 55, 150))
print(adicionar_minutos(9, 7, 4))
