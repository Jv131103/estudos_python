def inverter_string(s):
    uniao = ""
    for i in range(len(s) - 1, -1, -1):
        uniao += s[i]
    return uniao


def inverter_string2(s):
    return s[::-1]


def inverter_string3(s):
    return "".join(reversed(s))


print(inverter_string("texto"))
print(inverter_string2("texto"))
print(inverter_string3("texto"))
