cont = 0
while cont <= 10:
    print("*" * cont)
    cont += 1

cont = 9
while cont > 0:
    print("*" * cont)
    cont -= 1

print()

cont = 1
while cont <= 10:
    for i in range(cont):
        print("*", end="")
    print()
    cont += 1

cont = 9
while cont > 0:
    for i in range(cont):
        print("*", end="")
    print()
    cont -= 1
