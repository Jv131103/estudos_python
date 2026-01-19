"""
Substring sem caracteres repetidos

Faça um programa que:

    Receba uma string

    Encontre o tamanho da maior substring sem caracteres repetidos

Exemplo:

    "abcabcbb" → 3  ("abc")

Janela cresce e contrai conforme repetição.
"""


def maior_substring_sem_repeticao(s: str) -> int:
    ultima_pos = {}   # char -> ultimo indice
    left = 0
    melhor = 0

    for right, ch in enumerate(s):
        # se ch já apareceu e está dentro da janela atual, contrai pela esquerda
        if ch in ultima_pos and ultima_pos[ch] >= left:
            left = ultima_pos[ch] + 1

        # registra/atualiza a última posição do caractere
        ultima_pos[ch] = right

        # atualiza o melhor tamanho
        tamanho = right - left + 1
        if tamanho > melhor:
            melhor = tamanho

    return melhor


print(maior_substring_sem_repeticao("abcabcbb"))  # 3
print(maior_substring_sem_repeticao("bbbbb"))     # 1
print(maior_substring_sem_repeticao("pwwkew"))    # 3 ("wke")
print(maior_substring_sem_repeticao(""))          # 0
