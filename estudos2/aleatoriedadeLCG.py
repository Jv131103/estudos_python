def lcg(seed, a=1103515245, c=12345, m=2**31):
    while True:
        seed = (a * seed + c) % m
        yield seed


gerador = lcg(seed=32)

for _ in range(5):
    print(next(gerador))
