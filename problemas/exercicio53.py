# minha versão
for i in range(1, 4):
    cont = 1

    while cont <= 10:
        print(cont)
        cont += 1

print("fim")

# versão da net
# solução 1
x = 1
for i in range(1, 11):
    print(i)
    if i == 10:
        while x <= 10:
            print(x)
            x += 1
            if x == 11:
                y = 1
                while y <= 10:
                    print(y)
                    y += 1
                    if y == 11:
                        print('Fim')

# solução 2
x = 11
for a in range(1, 4):
    for x in range(1, 11):
        print(x)
