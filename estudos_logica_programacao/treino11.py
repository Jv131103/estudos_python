x = float(input("Forneça um número entre 0 e 1: "))

if not (0 <= x <= 1):
    print("É obrigatório estar no intervalo entre 0 e 1")
else:

    teste = x * x

    print(f"x² = {teste:.4f}")

    if 0 < teste < 0.5:
        print("Valor insuficiente!")
    elif 0.5 <= teste < 0.7:
        print("Valor suficiente")
    elif 0.7 <= teste < 0.85:
        print("Valor bom")
    elif 0.85 <= teste < 0.95:
        print("Valor ótimo")
    else:
        print("Valor excelente")

print("\n\n---- FIM ----")
