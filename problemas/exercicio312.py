def intervalo(inicio, fim, intervalo=1):
    lista = []
    if inicio < fim:
        for i in range(inicio, fim + 1, intervalo):
            lista.append(i)
    else:
        for i in range(inicio, fim - 1, -intervalo):
            lista.append(i)

    return lista


print(intervalo(2, 6))
print(intervalo(6, 2))
