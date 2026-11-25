def pode_entrar(idade, tem_ingresso, acompanhado):
    if tem_ingresso:
        if idade >= 16:
            return True
        elif acompanhado:
            return True

    return False


print(pode_entrar(18, True, False))
print(pode_entrar(14, True, True))
print(pode_entrar(14, True, False))
print(pode_entrar(20, False, True))
print(pode_entrar(16, True, False))
print(pode_entrar(10, False, True))
print(pode_entrar(15, True, True))
print(pode_entrar(17, True, False))
