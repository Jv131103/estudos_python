soma = 0
quantidade = 0

while True:
    try:
        numero = int(input("Digite um número: "))

        if numero == 0:
            break

        soma += numero
        quantidade += 1
    except ValueError:
        print("Digite um número válido!")
        continue


print(f"Soma: {soma}")
print(f"Quantidade: {quantidade}")

if quantidade > 0:
    media = soma / quantidade
    print(f"Média: {media:.2f}")
else:
    print("Média: não há números para calcular.")
