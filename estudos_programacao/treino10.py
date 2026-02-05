x = int(input("Forneça um número entre 0 e 10: "))

if x < 0:
    print("X - Inválido (negativo)")
elif x >= 0 and x <= 5:
    print("X na faixa 0-3 (Abaixo do Ideal)")
elif x >= 4 and x <= 7:
    print("X na faixa 4-7 (Faixa ideal)")
elif x >= 8 and x <= 10:
    print("X na faixa 8 - 10 (Acima da faixa ideal)")
else:
    print("X - Inválido (maior que 10)")

print("\n\n---- FIM ----")
