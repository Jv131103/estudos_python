nota1 = float(input("Nota 1 (de 0 e 10): "))
if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Nota 2 (de 0 e 10): "))
    if not (nota2 < 0 or nota2 > 10):
        media = (nota1 + nota2) / 2
        print(f"Media = {media:.2f}")
    else:
        print(f"A '{nota2}' é inválida!")
else:
    print(f"A '{nota1}' é inválida!")
