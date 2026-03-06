valor = float(input("Valor: "))

if valor <= 1000:
    resultado = valor * 0.2
elif valor < 2000:
    resultado = valor * 1.3
else:
    resultado = valor + valor * 0.1

print(f"Resultado = {resultado}")
