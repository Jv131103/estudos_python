def fibonacci():
    x = 0
    y = 1
    while True:
        yield x
        x, y = y, x + y


gen = fibonacci()
primeiros = [next(gen) for _ in range(10)]
print(primeiros)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
