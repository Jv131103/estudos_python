"""
Tema: Sistema de pagamento

    Objetivo: chamar o mesmo método em objetos diferentes sem saber o tipo.

Requisitos

    Criar as classes:

        PagamentoCartao

        PagamentoPix

        PagamentoBoleto

    Todas devem ter o método:

        processar(valor)

    Comportamento esperado

        PagamentoCartao.processar(valor)
            → imprime: "Pagamento de R$X via cartão aprovado"

        PagamentoPix.processar(valor)
            → imprime: "Pagamento de R$X via PIX realizado"

        PagamentoBoleto.processar(valor)
            → imprime: "Boleto de R$X gerado"

Função polimórfica

    Criar uma função:

        def executar_pagamento(pagamento, valor):
            pagamento.processar(valor)

Regra importante

    A função não pode usar isinstance

    Não pode verificar o tipo do objeto

    Só confiar que o método existe
"""


class PagamentoCartao:
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via cartão aprovado")


class PagamentoPix:
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via PIX realizado")


class PagamentoBoleto:
    def processar(self, valor):
        print(f"Boleto de R$ {valor:.2f} gerado")


def executar_pagamento(pagamento, valor):
    pagamento.processar(valor)


if __name__ == "__main__":

    from random import randrange

    pagamentos = [PagamentoBoleto(), PagamentoCartao(), PagamentoPix()]
    for pagamento in pagamentos:
        executar_pagamento(pagamento, randrange(1, 1_000_000))
