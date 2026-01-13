"""
Situação:

    Um estacionamento cobra um valor fixo por hora.

Crie:

    Constante para valor da hora

    Variável para quantidade de horas

    Calcule o total

Depois:

    Mude a quantidade de horas

    Observe que a constante permanece a mesma
"""

VALOR_HORA = 12.5

qtd_horas = int(input("Quantas horas ficou? "))
qtd_minutos = int(input("Quantos minutos ficou? "))

final = qtd_horas + (qtd_minutos / 60)

total = final * VALOR_HORA
print(f"Valor final: R$ {total:.2f}")

print()

qtd_horas = int(input("Quantas horas ficou? "))
qtd_minutos = int(input("Quantos minutos ficou? "))

final = qtd_horas + (qtd_minutos / 60)
total = final * VALOR_HORA
print(f"Valor final: R$ {total:.2f}")
