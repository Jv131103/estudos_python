def look_and_say1(string):
    if not isinstance(string, str):
        raise TypeError("Objeto precisa ser do tipo string")
    elif not string.isdecimal():
        raise ValueError("String precisa ser de números")
    elif len(string) == 1:
        return f"1{string}"

    cont = 1
    saida = []
    for j in range(1, len(string)):
        if string[j - 1] == string[j]:
            cont += 1
        else:
            saida.extend([str(cont), string[j - 1]])
            cont = 1

    saida.extend([str(cont), string[j]])

    return "".join(saida)


def look_and_say2(string):
    if not string:
        return ""
    char = string[0]
    cont = len(string) - len(string.lstrip(char))
    return f"{cont}{char}" + look_and_say2(string[cont:])


if __name__ == "__main__":
    print(look_and_say1('1'))
    print(look_and_say1('11'))
    print(look_and_say1('21'))
    print(look_and_say1('221'))

    print()
    print(look_and_say2('1'))
    print(look_and_say2('11'))
    print(look_and_say2('21'))
    print(look_and_say2('221'))
