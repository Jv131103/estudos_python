def blum_blum_shub(seed, n):
    while True:
        seed = (seed * seed) % n
        yield seed


gerador = blum_blum_shub(seed=42, n=10)

for _ in range(5):
    print(next(gerador))
