def divisao_segura(a, b):
    if b == 0:
        print("Erro de divisão por 0!")
        return None

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Parâmetros a e b precisam ser de tipo numérico(int / float)!")
        return None

    return a / b


def divisao_segura2(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro de divisão por 0!")
        return None
    except TypeError:
        print("Parâmetros a e b precisam ser de tipo numérico (int / float)!")
        return None


print(divisao_segura(10, 2))
print(divisao_segura2(10, 2))
print(divisao_segura(10, 0))
print(divisao_segura2(10, 0))
print(divisao_segura(10, "a"))
print(divisao_segura2(10, "a"))
