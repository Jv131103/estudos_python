from dataclasses import dataclass


@dataclass
class RegraFrete:
    peso_min: float
    peso_max: float
    km_min: float
    km_max: float
    valor_base: float
    adicional_km: float


TABELA_FRETE = [
    RegraFrete(0.0, 5.0, 0.0, 100.0, 15.00, 0.05),
    RegraFrete(0.0, 5.0, 100.1, float('inf'), 15.00, 0.08),
    RegraFrete(5.1, 20.0, 0.0, 100.0, 30.00, 0.10),
    RegraFrete(5.1, 20.0, 100.1, float('inf'), 30.00, 0.15),
    RegraFrete(20.1, float('inf'), 0.0, float('inf'), 60.00, 0.20)
]


def calcular_frete(peso, distancia):
    for regra in TABELA_FRETE:
        if regra.peso_min <= peso <= regra.peso_max and regra.km_min <= distancia <= regra.km_max:
            km_excedente = max(0.0, distancia - 100.0)

            valor_final = regra.valor_base + (km_excedente * regra.adicional_km)
            return valor_final

    raise ValueError("Configuração de frete não encontrada para estes valores.")


# Testando o cenário do Exemplo 2 (4kg e 150km)
resultado = calcular_frete(peso=4.0, distancia=150.0)
print(f"Valor do Frete: R$ {resultado:.2f}")
