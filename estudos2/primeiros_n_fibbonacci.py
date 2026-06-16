def fibonacci(limite):
    x = 1
    y = 1
    cont = 1
    print(y, end=" ")
    while cont < limite:
        x, y = y, x + y
        print(x, end=" ")
        cont += 1
    print()


fibonacci(100)
