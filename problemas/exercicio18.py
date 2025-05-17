"""
Faça um programa, com uma função que dado uma lista e uma posiçãoda mesma,
faça o quartil dessa posição

    p_index = int(p * len(lista))
"""


def quartil(lista, posicao):
    lista = sorted(lista)
    p_index = int(posicao * len(lista))
    return lista[p_index]


if __name__ == "__main__":
    lista = [2, 4, 6, 8, 10, 12, 14, 16]
    print(quartil(lista, 0.25))  # Deve imprimir 6
    print(quartil(lista, 0.5))   # Deve imprimir 10
    print(quartil(lista, 0.75))  # Deve imprimir 14
