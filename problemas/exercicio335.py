class Lista:
    def __init__(self, lista) -> None:
        self.lista = lista

    def imprimir_pares(self):
        i = 0
        j = len(self.lista) - 1

        while i < j:
            print(self.lista[i], self.lista[j])
            i += 1
            j -= 1


li = Lista([2, 4, 6, 8, 10, 12])
li.imprimir_pares()
