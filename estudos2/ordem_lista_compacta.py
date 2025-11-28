def lista_esta(seq):
    if not isinstance(seq, list):
        return "Tipo Incompatível"

    if not seq:
        return "Vazia"

    crescente = all(x <= y for x, y in zip(seq, seq[1:]))
    decrescente = all(x >= y for x, y in zip(seq, seq[1:]))

    if crescente and not decrescente:
        return "Crescente"
    elif decrescente and not crescente:
        return "Decrescente"
    else:
        return "Desordenada"


listas = [
    [1, 2, 3, 4],
    [1, 3, 5, 7],
    [1, 6, 5, 7],
    [10, 8, 5, 1],
    [5, 4, 3, 2, 1],
    [],
    [0, 0, 0, 0, 0, 0],
    [1, 5, 3, 7],
    ""
]

for lista in listas:
    print(f"Resultado da lista {lista}: {lista_esta(lista)}")
