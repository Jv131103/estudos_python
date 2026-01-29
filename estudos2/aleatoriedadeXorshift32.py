def xorshift32(seed):
    while True:
        seed ^= (seed << 13) & 0xFFFFFFFF
        seed ^= (seed >> 17)
        seed ^= (seed << 5) & 0xFFFFFFFF
        yield seed


gerador = xorshift32(seed=22)

for _ in range(5):
    print(next(gerador))
