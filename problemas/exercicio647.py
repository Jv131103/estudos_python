"""
Crie uma classe Conversor com métodos estáticos
para converter km → m e m → km.
"""


class Conversor:
    @staticmethod
    def km_para_m(valor):
        return valor * 1000

    @staticmethod
    def m_para_km(valor):
        return valor / 1000


print(Conversor.km_para_m(1))
print(Conversor.m_para_km(1000))
