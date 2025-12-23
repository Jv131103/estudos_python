class Texto:
    def __init__(self, string) -> None:
        self.string = string

    def comparar_extremos(self):
        i = 0
        j = len(self.string) - 1

        while i < j:
            print(self.string[i], self.string[j])
            i += 1
            j -= 1


tex = Texto("radar")
tex.comparar_extremos()
