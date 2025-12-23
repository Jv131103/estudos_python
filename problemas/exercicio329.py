def mostrar_ponteiros(string):
    i = 0
    j = len(string) - 1

    while i < j:
        print(string[i], string[j])
        i += 1
        j -= 1


mostrar_ponteiros('radar')
