lista = [
    944, 52, 161, 436, 77, 217, 616, 639, 280, 277, 907, 735, 321,
    194, 736, 130, 793, 148, 799, 631, 906, 417, 186, 913, 446, 537, 86, 75,
    328, 77, 899, 481, 303, 997, 212, 217, 696, 391, 402, 800, 709, 293, 9,
    700, 108, 253, 562, 166, 252, 315, 655, 680, 944, 8, 850, 765, 821, 216,
    685, 666, 860, 32, 492, 880, 714, 424, 270, 308, 641, 83, 555, 807, 840,
    724, 193, 256, 556, 665, 902, 714, 564, 13, 903, 625, 14, 551, 301, 915,
    633, 781, 427, 517, 372, 164, 469, 194, 5, 818, 776,
]

# versao 1
qtd_pares = 0
qtd_impares = 0

for valor in lista:
    if valor % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1


print(f"Quantidade pares: {qtd_pares}")
print(f"Quantidade impares: {qtd_impares}")


# versao 2
lista_par = [numero for numero in lista if numero % 2 == 0]
lista_impar = [numero for numero in lista if numero % 2 != 0]
print(f'Quantidade de números pares: {len(lista_par)}')
print(f'Quantidade de números pares: {len(lista_impar)}')
