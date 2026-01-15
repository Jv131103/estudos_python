def isfloating(string):
    string = string.replace(",", ".").replace("-", "").replace("+", "")
    if "." not in string:
        return False

    casas = string.split(".")

    if len(casas) != 2:
        return False

    esquerda, direita = casas

    for valor in esquerda:
        if valor not in "0123456789":
            return False

    for valor in direita:
        if valor not in "0123456789":
            return False

    return True


print(isfloating("3.14"))
print(isfloating("3,14"))
print(isfloating("0.5"))
print(isfloating(".5"))
print(isfloating("5."))
print(isfloating("10.25"))
print(isfloating("3..14"))
print(isfloating("-3.14"))
print(isfloating("+3,14"))
print(isfloating("+3,14"))
print(isfloating("3-14"))
print(isfloating("3+14"))
print(isfloating("++3.14"))
print(isfloating("--3.14"))
