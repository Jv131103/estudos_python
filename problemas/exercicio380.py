def valida(expr):
    min_abertos = 0
    max_abertos = 0

    for ch in expr:
        if ch == "(":
            min_abertos += 1
            max_abertos += 1
        elif ch == ")":
            min_abertos = max(0, min_abertos - 1)
            max_abertos -= 1
        else:  # '*'
            min_abertos = max(0, min_abertos - 1)  # '*' pode virar ')'
            max_abertos += 1                        # ou virar '('

        if max_abertos < 0:
            return False

    return min_abertos == 0


print(valida("(*)"))   # True
print(valida("(*))"))  # True
print(valida("())*"))  # False
