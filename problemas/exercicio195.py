def maior_lista(lista):
    maior = lista[0]

    for i in lista:
        if i > maior:
            maior = i

    return maior


def menor_lista(lista):
    menor = lista[0]

    for i in lista:
        if i < menor:
            menor = i

    return menor


cont = 0
lista = []
while cont < 5:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Digite um valor numérico do tipo inteiro")
        continue

    lista.append(numero)
    cont += 1


maior = maior_lista(lista)
menor = menor_lista(lista)
ordenada = sorted(lista)

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Ordenada: {ordenada}")
