class MT19937:
    """
    Mersenne Twister MT19937 (32-bit) - implementação do zero.
    Gera inteiros de 32 bits e floats em [0,1).
    """

    # Parâmetros do MT19937
    w, n, m, r = 32, 624, 397, 31
    a = 0x9908B0DF

    u, d = 11, 0xFFFFFFFF
    s, b = 7, 0x9D2C5680
    t, c = 15, 0xEFC60000
    l = 18

    f = 1812433253

    lower_mask = (1 << r) - 1              # últimos r bits
    upper_mask = (~lower_mask) & 0xFFFFFFFF  # primeiros (w-r) bits

    def __init__(self, seed: int = 5489):
        self.MT = [0] * self.n
        self.index = self.n
        self.seed(seed)

    def seed(self, seed: int):
        """Inicializa o estado interno com uma seed."""
        seed &= 0xFFFFFFFF
        self.index = self.n
        self.MT[0] = seed
        for i in range(1, self.n):
            prev = self.MT[i - 1]
            self.MT[i] = (self.f * (prev ^ (prev >> (self.w - 2))) + i) & 0xFFFFFFFF

    def _twist(self):
        """Gera os próximos 624 valores do estado."""
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i + 1) % self.n] & self.lower_mask)
            xA = (x >> 1) & 0xFFFFFFFF
            if x & 1:
                xA ^= self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA

        self.index = 0

    def random_uint32(self) -> int:
        """Retorna um inteiro de 32 bits (0 .. 2^32-1)."""
        if self.index >= self.n:
            self._twist()

        y = self.MT[self.index]
        self.index += 1

        # Tempering (melhora distribuição)
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= (y >> self.l)

        return y & 0xFFFFFFFF

    def random(self) -> float:
        """Float em [0,1). Usa 32 bits de aleatoriedade."""
        return self.random_uint32() / 2**32

    def randrange(self, n: int) -> int:
        """
        Inteiro uniforme em [0, n) sem viés (rejection sampling).
        """
        if n <= 0:
            raise ValueError("n deve ser > 0")

        threshold = (-n) % n
        while True:
            r = self.random_uint32()
            if r >= threshold:
                return r % n


# ----------------- Exemplo de uso -----------------
if __name__ == "__main__":
    rng = MT19937(seed=42)

    print("5 uint32:")
    for _ in range(5):
        print(rng.random_uint32())

    print("\n5 floats [0,1):")
    for _ in range(5):
        print(rng.random())

    print("\n10 valores em [0, 10):")
    for _ in range(10):
        print(rng.randrange(10), end=" ")
    print()
