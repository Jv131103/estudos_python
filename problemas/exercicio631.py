"""
ContaBancaria com saldo protegido e operações seguras

Objetivo: encapsular _saldo e impedir alterações diretas.

Crie uma classe Conta Bancária

    saldo precisa ser protegido

        começa em 0

    Deve-se haver somente leitura e sem setter

    Métodos:

        depositar(valor) (valor > 0)

        sacar(valor) (valor > 0 e não pode sacar mais do que o saldo)

    Criar exceções personalizadas:

        ValorInvalidoError

        SaldoInsuficienteError

    método extrato() retorna string tipo: "Saldo atual: R$ 123.45"
"""


class ErroContaBancaria(Exception):
    """Erro mãe da conta"""
    pass


class ValorInvalidoError(ErroContaBancaria):
    """Para tipagem"""
    pass


class SaldoInsuficienteError(ErroContaBancaria):
    """Para saldo excessivo ou insuficiente"""
    pass


class ContaBancaria:
    """
    Simula uma conta bancária real

        entrada de dados:

            saldo: 0.0 (PROTEGIDO)

        retorna o valor atual do saldo na conta

    REGRAS:

        - Saldo inicia em 0, mas pode ser alterado

        - É proibido fazer inserção de saldo a unha. Use os métodos ou na própria definição da conta a inserção do saldo

        - Saldo precisa ser exclusivamente um valor do tipo numérico

        - Não pode fazer depósitos de valores <= 0

        - Não pode fazer saque de valores <= 0

        - Não pode fazer saque de valores > saldo_atual

        - retorna extrato: Bônus

    """
    def __init__(self, saldo: int | float = 0.0) -> None:
        if not isinstance(saldo, (int, float)):
            raise ValorInvalidoError("Saldo inicial deve ser numérico")
        if saldo < 0:
            raise ValorInvalidoError("Saldo inicial não pode ser negativo")
        self._saldo = saldo

    @property
    def saldo(self) -> int | float:
        '''Apenas interface, modo de leitura'''
        return self._saldo

    def depositar(self, valor: int | float) -> None:
        '''
        Realiza depósito de um valor para a conta

        Regras:

            - Saldo precisa ser exclusivamente um valor do tipo numérico

            - Não pode fazer depósitos de valores <= 0
        '''
        if not isinstance(valor, (int, float)):
            raise ValorInvalidoError("valor precisa ser numérico")

        if valor <= 0:
            raise SaldoInsuficienteError("Valor não pode ser negativo!\nDEPÓSITO CANCELADO POR INSUFICIENCIA DE VALOR")

        self._saldo += valor

    def sacar(self, valor: int | float) -> None:
        '''
        Realiza saque de um valor da conta

        Regras:

            - Saldo precisa ser exclusivamente um valor do tipo numérico

            - Não pode fazer saque de valores <= 0

            - Não pode fazer saque de valores > saldo_atual
        '''
        if not isinstance(valor, (int, float)):
            raise ValorInvalidoError("valor precisa ser numérico")

        if valor <= 0:
            raise SaldoInsuficienteError("Valor não pode ser negativo!\nSAQUE CANCELADO POR INSUFICIENCIA DE VALOR")

        if valor > self.saldo:
            raise SaldoInsuficienteError("Valor não pode ser maior que o saldo atual da conta!\nSAQUE CANCELADO POR EXCESSO DE VALOR")

        self._saldo -= valor

    def extrato(self) -> str:
        """Visualização padrão de saída"""
        return f"Saldo atual: R$ {self.saldo:.2f}"


if __name__ == "__main__":
    c1 = ContaBancaria()

    print(c1.extrato())

    c1.depositar(2000)

    print(c1.saldo)

    c1.sacar(1000)

    print(c1.extrato())
