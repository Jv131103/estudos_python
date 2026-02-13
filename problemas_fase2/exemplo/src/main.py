# versao procedural
def contar_unicos_simples(texto: str) -> int:
    vistos = []

    for letra in texto:
        if letra not in vistos:
            vistos.append(letra)

    return len(vistos)


# versao otimizada / funcional
def contar_unicos_otimizado(texto: str) -> int:
    return len(set(texto))


# Versão POO
class ContadorDeCaracteres:

    def __init__(self, texto: str):
        self.texto = texto

    def contar_simples(self) -> int:
        vistos = []

        for letra in self.texto:
            if letra not in vistos:
                vistos.append(letra)

        return len(vistos)

    def contar_otimizado(self) -> int:
        return len(set(self.texto))
