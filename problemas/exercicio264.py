def qtd_string(string):
    return len(string)


def qtd_string2(string):
    qtd = 0
    for _ in string:
        qtd += 1
    return qtd


string = "Python"
print(qtd_string(string))
print(qtd_string2(string))
