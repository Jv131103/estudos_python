multiplos3e5 = list(
    map(lambda i: i if i % 3 == 0 or i % 5 == 0 else round(i**(1 / 2), 2), range(1, 51))
)

print(multiplos3e5)
