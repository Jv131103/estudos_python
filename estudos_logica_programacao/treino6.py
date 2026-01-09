area_desejada = float(input())  # metrao quadrados

lado = area_desejada / 2          # chute inicial
iteracoes = 0

while lado * lado < area_desejada:
    lado *= 1.005   # aumento de 0,5%
    iteracoes += 1

print(f"Lado aproximado: {lado:.4f} m")
print(f"Área obtida: {lado * lado:.4f} m²")
print(f"Iterações: {iteracoes}")
