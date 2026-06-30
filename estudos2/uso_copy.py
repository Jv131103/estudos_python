a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

# A referência se mantém, por que a cópia não foi interna, mas externa
print(a)
print(b)
