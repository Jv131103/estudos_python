"""
Faça um programa que:

    Crie um buffer circular de tamanho fixo 5

    Receba uma sequência de números maior que 5

    Insira os números no buffer

    Quando o buffer estiver cheio:

        sobrescreva o valor mais antigo

Ao final, mostre o estado final do buffer

Exemplo conceitual:

    Buffer tamanho 5
    Entrada: [10, 20, 30, 40, 50, 60, 70]

    Resultado final:
    [60, 70, 30, 40, 50]


(a posição exata depende da lógica de rotação)
"""


def buffer_circular(entrada, tamanho_buffer=5):
    if not entrada:
        return None

    buffer = [None] * tamanho_buffer
    pos = 0  # posição atual de escrita

    for valor in entrada:
        buffer[pos] = valor
        pos = (pos + 1) % tamanho_buffer

    return buffer


print(buffer_circular([10, 20, 30, 40, 50, 60, 70]))
