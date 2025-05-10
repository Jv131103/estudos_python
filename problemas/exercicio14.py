"""

Faça um programa que dada a entrada de uma lista, ele faça o cálculo da mesma:

    Exemplo de entrada: [1, 2, 3, 4]

    Exemplo de saída: [1, 3, 6, 10]

"""

lista_original = [1, 2, 3, 4]
lista_acumulada = []

soma = 0
for itens in lista_original:
    soma += itens
    lista_acumulada.append(soma)

print(f"Lista Acumulada: {lista_acumulada}")
print(f"Soma final: {soma}")
