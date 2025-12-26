def teve_faltas(faltas):
    return faltas >= 10


def nota_maior_que_7(nota):
    return nota >= 7


def avaliar(nota, faltas):
    if nota_maior_que_7(nota) and not teve_faltas(faltas):
        return "Aprovado"
    elif not nota_maior_que_7(nota) and not teve_faltas(faltas):
        return "Recuperação"
    elif nota_maior_que_7(nota) and teve_faltas(faltas):
        return "Reprovado por faltas"
    else:
        return "Reprovado"


def avaliar1(nota, faltas):
    aprovado_nota = nota >= 7
    faltou = faltas >= 10

    if aprovado_nota and not faltou:
        return "Aprovado"
    if not aprovado_nota and not faltou:
        return "Recuperação"
    if aprovado_nota and faltou:
        return "Reprovado por faltas"
    return "Reprovado"


print(avaliar(7, 0))
print(avaliar1(7, 0))
print(avaliar(5, 0))
print(avaliar1(5, 0))
print(avaliar(7, 10))
print(avaliar1(7, 10))
print(avaliar(5, 10))
print(avaliar1(5, 10))
