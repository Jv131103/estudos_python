def filtrar_maiores(lista, limite):
    return [lista[i] for i in range(len(lista)) if lista[i] > limite]


lista = list(range(100))
print(filtrar_maiores(lista, 10))
