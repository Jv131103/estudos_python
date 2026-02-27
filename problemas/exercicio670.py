"""
Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON
para desenvolver um trabalho em parceria: um serviço em que as pessoas possam
usar um estúdio profissional para gravar seus vídeos para o YouTube com
máxima qualidade. O serviço ganha dinheiro por meio de um sistema de
assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento
que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente,
o faturamento anual dele e que calcule e exiba qual o valor do bônus que
o cliente deve pagar a vocês. A tabela a seguir mostra a porcentagem de
acordo com cada nível de assinatura:

Nível	Porcentagem sobre o faturamento
Basic       30%
Silver      20%
Gold        10%
Platinum    5%
"""


def faturamento(assinatura, faturamento):
    niveis = {
        "basic": 0.3,
        "silver": 0.2,
        "gold": 0.1,
        "platinum": 0.05
    }

    percent_bonus = niveis.get(assinatura, None)
    if not percent_bonus:
        return print("Assinatura inválida")

    retorno_empresa = faturamento * percent_bonus
    print(f"A empresa receberá: R$ {retorno_empresa:.2f} reais")
    resto_cliente = faturamento - retorno_empresa
    print(f"O cliente ficará com R$ {resto_cliente:.2f} reais")


faturamento("basic", 1000)
