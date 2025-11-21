def checar_lista1(lista):
    return not len(lista) > 0  # Caso a lista seja vazia será retornado True


def checar_lista2(lista):
    if not len(lista) > 0:
        return True
    else:
        return False


print(checar_lista1([]))
print(checar_lista1([10, 11, 12]))

print(checar_lista2([]))
print(checar_lista2([10, 11, 12]))
