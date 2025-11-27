class Temperatura:
    def __init__(self, valor):
        self.valor = valor

    def convert(self, _from="C", to="F"):
        _from = _from.upper()
        to = to.upper()

        # verificar unidades válidas
        unidades = ["C", "F", "K"]
        if _from not in unidades or to not in unidades:
            raise ValueError("Use apenas unidades: C, F ou K")

        # 1 converte TUDO para Kelvin
        para_kelvin = {
            "C": lambda v: v + 273.15,
            "F": lambda v: (v - 32) * 5 / 9 + 273.15,
            "K": lambda v: v
        }

        # 2 converte Kelvin para unidade final
        de_kelvin = {
            "C": lambda k: k - 273.15,
            "F": lambda k: (k - 273.15) * 9 / 5 + 32,
            "K": lambda k: k
        }

        # 1ª etapa: origem → Kelvin
        k = para_kelvin[_from](self.valor)

        # 2ª etapa: Kelvin → destino
        return de_kelvin[to](k)


class Tempo:
    def __init__(self, valor):
        self.valor = valor

    def convert(self, _from="H", to="M"):
        _from = _from.upper()
        to = to.upper()

        # verificar unidades válidas
        unidades = ["H", "M", "S"]
        if _from not in unidades or to not in unidades:
            raise ValueError("Use apenas unidades: H, M ou S")

        # unidade base: segundos (S)
        # converter tudo → segundos
        para_segundos = {
            "H": lambda v: v * 3600,  # horas → segundos
            "M": lambda v: v * 60,    # minutos → segundos
            "S": lambda v: v          # segundos → segundos
        }

        # converter segundos → destino
        de_segundos = {
            "H": lambda s: s / 3600,  # segundos → horas
            "M": lambda s: s / 60,    # segundos → minutos
            "S": lambda s: s          # segundos → segundos
        }

        # 1 converter origem → segundos
        segundos = para_segundos[_from](self.valor)

        # 2 converter segundos → destino final
        return de_segundos[to](segundos)


class Massa:
    def __init__(self, valor):
        self.valor = valor

    def convert(self, _from="KG", to="G"):
        _from = _from.upper()
        to = to.upper()

        unidades = ["MG", "G", "KG", "TON", "LB"]
        if _from not in unidades or to not in unidades:
            raise ValueError("Use unidades: MG, G, KG, TON, LB")

        # unidade base = KG
        para_kg = {
            "MG": lambda v: v / 1_000_000,
            "G": lambda v: v / 1000,
            "KG": lambda v: v,
            "TON": lambda v: v * 1000,
            "LB": lambda v: v * 0.453592
        }

        de_kg = {
            "MG": lambda kg: kg * 1_000_000,
            "G": lambda kg: kg * 1000,
            "KG": lambda kg: kg,
            "TON": lambda kg: kg / 1000,
            "LB": lambda kg: kg / 0.453592
        }

        # 1 orig → kg
        kg = para_kg[_from](self.valor)

        # 2 kg → destino
        return de_kg[to](kg)


class Volume:
    def __init__(self, valor):
        self.valor = valor

    def convert(self, _from="L", to="ML"):
        _from = _from.upper()
        to = to.upper()

        unidades = ["ML", "L", "M3", "CM3"]
        if _from not in unidades or to not in unidades:
            raise ValueError("Use unidades: ML, L, M3, CM3")

        # unidade base = Litro
        para_litro = {
            "ML": lambda v: v / 1000,
            "L": lambda v: v,
            "M3": lambda v: v * 1000,
            "CM3": lambda v: v / 1000
        }

        de_litro = {
            "ML": lambda l: l * 1000,
            "L": lambda l: l,
            "M3": lambda l: l / 1000,
            "CM3": lambda l: l * 1000
        }

        # 1 orig → litro
        l = para_litro[_from](self.valor)

        # 2 litro → destino
        return de_litro[to](l)


class InterfaceConversor:
    def __init__(self):
        # só para ter as unidades organizadas aqui
        self.unidades_temp = ["C", "F", "K"]
        self.unidades_tempo = ["H", "M", "S"]
        self.unidades_massa = ["MG", "G", "KG", "TON", "LB"]
        self.unidades_volume = ["ML", "L", "M3", "CM3"]

    def ler_float(self, msg):
        while True:
            try:
                return float(input(msg))
            except ValueError:
                print("Valor inválido! Digite um número.\n")

    def escolher_unidade(self, unidades):
        while True:
            print("Unidades disponíveis:")
            for i, u in enumerate(unidades, start=1):
                print(f"{i} - {u}")

            try:
                opc = int(input("Escolha a unidade: "))
                if 1 <= opc <= len(unidades):
                    return unidades[opc - 1]
                else:
                    print("Opção de unidade inválida!\n")
            except ValueError:
                print("Digite apenas números!\n")

    def menu_principal(self):
        print("=" * 50)
        print(" CONVERSOR DE UNIDADES ")
        print("=" * 50)
        print("1 - Temperatura (C, F, K)")
        print("2 - Tempo (H, M, S)")
        print("3 - Massa (MG, G, KG, TON, LB)")
        print("4 - Volume (ML, L, M3, CM3)")
        print("0 - Sair")

    # --------- cada tipo de conversão ----------

    def converter_temperatura(self):
        print("\n=== CONVERSOR DE TEMPERATURA ===")
        valor = self.ler_float("Digite o valor da temperatura: ")

        print("\nUnidade de origem:")
        u_from = self.escolher_unidade(self.unidades_temp)

        print("\nUnidade de destino:")
        u_to = self.escolher_unidade(self.unidades_temp)

        t = Temperatura(valor)
        resultado = t.convert(u_from, u_to)
        print(f"\n{valor} {u_from} = {resultado} {u_to}\n")

    def converter_tempo(self):
        print("\n=== CONVERSOR DE TEMPO ===")
        valor = self.ler_float("Digite o valor do tempo: ")

        print("\nUnidade de origem:")
        u_from = self.escolher_unidade(self.unidades_tempo)

        print("\nUnidade de destino:")
        u_to = self.escolher_unidade(self.unidades_tempo)

        tempo = Tempo(valor)
        resultado = tempo.convert(u_from, u_to)
        print(f"\n{valor} {u_from} = {resultado} {u_to}\n")

    def converter_massa(self):
        print("\n=== CONVERSOR DE MASSA ===")
        valor = self.ler_float("Digite o valor da massa: ")

        print("\nUnidade de origem:")
        u_from = self.escolher_unidade(self.unidades_massa)

        print("\nUnidade de destino:")
        u_to = self.escolher_unidade(self.unidades_massa)

        m = Massa(valor)
        resultado = m.convert(u_from, u_to)
        print(f"\n{valor} {u_from} = {resultado} {u_to}\n")

    def converter_volume(self):
        print("\n=== CONVERSOR DE VOLUME ===")
        valor = self.ler_float("Digite o valor do volume: ")

        print("\nUnidade de origem:")
        u_from = self.escolher_unidade(self.unidades_volume)

        print("\nUnidade de destino:")
        u_to = self.escolher_unidade(self.unidades_volume)

        v = Volume(valor)
        resultado = v.convert(u_from, u_to)
        print(f"\n{valor} {u_from} = {resultado} {u_to}\n")

    # -------------- loop principal --------------

    def executar(self):
        while True:
            self.menu_principal()
            try:
                opc = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida! Digite um número.\n")
                continue

            if opc == 1:
                self.converter_temperatura()
            elif opc == 2:
                self.converter_tempo()
            elif opc == 3:
                self.converter_massa()
            elif opc == 4:
                self.converter_volume()
            elif opc == 0:
                print("Saindo do conversor... Até mais!")
                break
            else:
                print("Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    app = InterfaceConversor()
    app.executar()
