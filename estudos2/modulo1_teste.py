def modulo(numero):
    if numero > 5:
        if numero < 10:
            return "Valor 1"
        else:
            return "Valor 2"
    elif numero < 0:
        return "Valor 3"
    else:
        return "Valor 4"


print(modulo(5))
