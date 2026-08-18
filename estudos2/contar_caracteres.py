import string as strin


def contar_caracteres(string):
    if not string:
        return {}

    string = string.lower().replace(" ", "").strip()
    for p in strin.punctuation:
        string = string.replace(p, "")

    d = {}
    for char in string:
        d[char] = d.get(char, 0) + 1

    return d


def contar_caracteres2(string):
    if not string:
        return {}

    string = string.lower().replace(" ", "").strip()

    d = {}
    for char in string:
        if char.isalnum():
            d[char] = d.get(char, 0) + 1

    return d


def contar_caracteres3(string):
    if not string:
        return {}

    string = string.lower().replace(" ", "").strip()

    d = {}
    for char in string:
        if char.isalnum():
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

    return d


print(contar_caracteres("Python Python"))
print(contar_caracteres2("Python Python"))
print(contar_caracteres3("Python Python"))
