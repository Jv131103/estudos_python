import timeit

from main import (reversao_manual_eficiente, reversao_slicing_manual,
                  reversao_slicing_manual_pythonico,
                  reversao_tecnica_dois_ponteiros,
                  reversao_tecnica_dois_ponteiros_lista,
                  reversao_tecnica_slicing_pythonico,
                  reversao_tecnica_slicing_reverse,
                  reverse_divide_conquer_join)

texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" * 100_000

funcoes = [
    ("manual", reversao_slicing_manual),
    ("manual_pythonico", reversao_slicing_manual_pythonico),
    ("manual_eficiente", reversao_manual_eficiente),
    ("dois_ponteiros", reversao_tecnica_dois_ponteiros),
    ("dois_ponteiros_lista", reversao_tecnica_dois_ponteiros_lista),
    ("slicing", reversao_tecnica_slicing_pythonico),
    ("reversed", reversao_tecnica_slicing_reverse),
    ("div_and_conquer", reverse_divide_conquer_join)
]

for nome, func in funcoes:
    tempo = timeit.timeit(lambda: func(texto), number=3)
    print(f"{nome:25}: {tempo:.4f} segundos")
