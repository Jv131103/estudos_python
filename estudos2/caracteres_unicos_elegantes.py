def caracteres_unicos(s):
    s = s.lower().strip()
    vistos = set()

    for char in s:
        if char in vistos:
            return False
        vistos.add(char)

    return True


def caracteres_unicos2(s):
    s = s.lower().strip()
    return len(s) == len(set(s))


print(caracteres_unicos("python"))
print(caracteres_unicos("banana"))
print()
print(caracteres_unicos2("python"))
print(caracteres_unicos2("banana"))
