"""
Viajar é bom demais! Uma agência de viagens está propondo uma estratégia
para alavancar as vendas após os impactos da pandemia do coronavírus.

A empresa ofertará descontos progressivos na compra de pacotes, dependendo do
número de viajantes que estão no mesmo grupo e moram na mesma residência.

Para ajudar a tornar esse projeto real, você deve criar um algoritmo que
receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a
QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos
de acordo com a tabela a seguir:

Categoria	    DESCONTOS

Econômica       2 viajantes 3%
	            3 viajantes 4%
	            4 viajantes ou mais 5%

Executiva       2 viajantes 5%
	            3 viajantes 7%
                4 viajantes ou mais 8%

Primeira classe  2 viajantes 10%
                 3 viajantes 15%
	             4 viajantes ou mais 20%

O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado),
o VALOR DO DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos)
e o VALOR MÉDIO POR VIAJANTE.
"""


def realizar_desconto_viagem(valor_pacote, categoria, qtd_passageiros):
    if qtd_passageiros < 2:
        desconto = 0

    elif categoria == "economica":
        option = {
            2: 0.03,
            3: 0.04,
        }

        desconto = option.get(qtd_passageiros, 0.05)

    elif categoria == "executiva":
        option = {
            2: 0.05,
            3: 0.07,

        }
        desconto = option.get(qtd_passageiros, 0.08)

    elif categoria == "primeira_classe":
        option = {
            2: 0.1,
            3: 0.15
        }
        desconto = option.get(qtd_passageiros, 0.2)

    else:
        return print("Categoria inválida!")

    print(f"Valor Bruto: R$ {valor_pacote:.2f}")

    percentual_desconto = valor_pacote * desconto
    print(f"Valor do desconto: R$ {percentual_desconto:.2f}")

    valor_liquido = valor_pacote - percentual_desconto
    print(f"Valor líquido: R$ {valor_liquido:.2f}")

    valor_medio_por_viajem = valor_liquido / qtd_passageiros
    print(f"Valor Médio: R$ {valor_medio_por_viajem:.2f}")


realizar_desconto_viagem(12000, "executiva", 10)
