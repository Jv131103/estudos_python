pesos_pecas = [500.2, 498.5, 501.1, 492.0, 500.0, 489.5]

pecas_rejeitadas = 0  # <-- CONTADORA (começa em zero absoluto)

for peso in pesos_pecas:
    if peso < 495.0:
        pecas_rejeitadas += 1  # Registra o evento de falha

print(f"Total de peças descartadas: {pecas_rejeitadas}")
# Saída: Total de peças descartadas: 2 (peças com 492.0 e 489.5)
