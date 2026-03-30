def aaa(num):
    return num + 4


def bbb(num):
    return aaa(num) - 2


def ccc(num):
    return bbb(num) * 3


print(f"Valor = {ccc(10)}")
