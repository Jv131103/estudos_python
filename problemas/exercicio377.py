def tem_texto(s):
    for c in s:
        if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
            return True
    return False


def tem_numero(s):
    for c in s:
        if c >= '0' and c <= '9':
            return True
    return False


def ok(s):
    if s is None or len(s) < 8 or not tem_texto(s) or not tem_numero(s):
        return False
    return True


print(ok(None))
print(ok(''))
print(ok('Ola1234'))
print(ok('sotemletraaqui'))
print(ok('123456789'))
print(ok('Acesso1993@s'))
