lista = [1, 2, 3, 4]

it = iter(lista)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
