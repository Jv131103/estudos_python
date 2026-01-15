num = int(input())

if num < 2:
    print("Não é primo")
else:
    cont = 2
    while cont < num:
        if num % cont == 0:
            print("Não é primo")
            break
        cont += 1
    else:
        print("É primo")
