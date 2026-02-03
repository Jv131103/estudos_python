"""
Crie um script que:

    imprima "Início"

    espere 2 segundos

    imprima "Fim"

Faça com time
"""

import time

inicio = time.time()
print(f"Tempo inicial: {inicio:.2f}")

time.sleep(2)

fim = time.time()
print(f"Tempo final: {fim:.2f}")

print(f"Tempo gasto: {fim - inicio:.2f} segundos")
