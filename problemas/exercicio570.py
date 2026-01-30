"""
Faça um programa que:

    Leia números inteiros um por vez (simule com uma lista fixa)

    Use um buffer de tamanho 3

    Sempre que o buffer atingir o tamanho máximo:

        some os valores do buffer

        imprima o resultado

        esvazie o buffer

    Ao final, se restarem valores no buffer, processe também

Exemplo conceitual:

    Entrada: [1, 2, 3, 4, 5, 6, 7]

    Processamento:
    [1,2,3] → soma = 6
    [4,5,6] → soma = 15
    [7]     → soma = 7
"""

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]

buffer = []

for valor in entrada:
    buffer.append(valor)
    if len(buffer) == 3:
        print(sum(buffer))
        buffer.clear()

# PEGA OS RESTANTES
if buffer:
    print(sum(buffer))
