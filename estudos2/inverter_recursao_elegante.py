def inverter_recursivo(s):
    if s == "":
        return ""
    return s[-1] + inverter_recursivo(s[:-1])


print(inverter_recursivo("python"))
