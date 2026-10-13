def collatz(numero):
    lista = [numero]
    maior = numero
    passo = 0
    while numero != 1:
        if numero % 2 == 0:
            numero //= 2
        else:
            numero *= 3
            numero += 1

        lista.append(numero)
        if numero > maior:
            maior = numero

        passo += 1

    return lista, maior, passo


numeros = [6, 3, 1, 27]
for numero in numeros:
    sequencia, maior_val, qtd_passos = collatz(numero)
    print(f"Sequência {sequencia}")
    print(f"Quantidade de passos: {qtd_passos}")
    print(f"Maior valor atingido: {maior_val}")
    print()
