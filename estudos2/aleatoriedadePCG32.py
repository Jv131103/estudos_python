class PCG32:
    """
    Implementação PCG-XSH-RR (PCG32).

    - Estado interno: 64 bits
    - Stream/sequence: define uma sequência independente (incremento ímpar)
    - Saída: 32 bits
    """

    def __init__(self, seed: int = 42, stream: int = 54):
        self.state = 0
        # inc precisa ser ímpar (PCG usa (stream << 1) | 1)
        self.inc = ((stream & 0xFFFFFFFFFFFFFFFF) << 1) | 1
        self.seed(seed)

    def seed(self, seed: int):
        """Inicializa estado de forma padrão (como recomendado no PCG)."""
        self.state = 0
        self._next_uint32()  # avança uma vez
        self.state = (self.state + (seed & 0xFFFFFFFFFFFFFFFF)) & 0xFFFFFFFFFFFFFFFF
        self._next_uint32()  # avança de novo

    @staticmethod
    def _rotr32(x: int, r: int) -> int:
        """Rotate-right 32 bits."""
        return ((x >> r) | (x << ((-r) & 31))) & 0xFFFFFFFF

    def _next_uint32(self) -> int:
        """
        Gera uint32 e atualiza estado:
        state = state * MULT + inc (mod 2^64)
        output = rotr32(xorshifted, rot)
        """
        oldstate = self.state

        # LCG 64-bit
        self.state = (oldstate * 6364136223846793005 + self.inc) & 0xFFFFFFFFFFFFFFFF

        # Permutação XSH-RR
        xorshifted = (((oldstate >> 18) ^ oldstate) >> 27) & 0xFFFFFFFF
        rot = (oldstate >> 59) & 31
        return self._rotr32(xorshifted, rot)

    def random_uint32(self) -> int:
        """Retorna inteiro no intervalo [0, 2^32)."""
        return self._next_uint32()

    def random(self) -> float:
        """Float em [0.0, 1.0). Usa 32 bits de aleatoriedade."""
        return self.random_uint32() / 2**32

    def randrange(self, n: int) -> int:
        """
        Inteiro uniforme em [0, n) sem viés (rejection sampling).
        """
        if n <= 0:
            raise ValueError("n deve ser > 0")

        # threshold = (-n) % n em aritmética 32-bit
        threshold = (-n) % n

        while True:
            r = self.random_uint32()
            if r >= threshold:
                return r % n


# ----------------- Exemplo de uso -----------------
if __name__ == "__main__":
    rng = PCG32(seed=42, stream=54)

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
