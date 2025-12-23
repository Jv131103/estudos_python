def somar_dois_ponteiros(lista):
    i = 0
    j = len(lista) - 1

    while i < j:
        print(f"{lista[i]} + {lista[j]} = {lista[i] + lista[j]}")
        i += 1
        j -= 1


somar_dois_ponteiros([1, 2, 3, 4, 5])
