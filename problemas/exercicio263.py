def nums_maiores_que_cinco(lista):
    return len([i for i in lista if i > 5])


lista = list(range(0, 11))
print(nums_maiores_que_cinco(lista))
