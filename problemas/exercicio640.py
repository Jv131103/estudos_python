"""
Tema: Monitoramento de sistema

Objetivo: garantir que todas as classes sigam um contrato comum.

Requisitos:

    Criar uma classe abstrata Monitor

        método abstrato:
            coletar_dados()

    Criar implementações:

        MonitorCPU

        MonitorMemoria

        MonitorDisco

    Comportamento esperado:

        Cada classe retorna uma string diferente, por exemplo:

            "Uso de CPU: 45%"

            "Uso de memória: 68%"

            "Uso de disco: 72%"

    Função polimórfica

        Criar uma função:

            def exibir_status(monitores):
                for monitor in monitores:
                    print(monitor.coletar_dados())

Regra importante

    exibir_status não sabe qual monitor está usando

    Só chama o método comum

    Todas as classes são obrigadas a implementar coletar_dados
"""
from abc import ABC, abstractmethod

import psutil


class MonitorError(Exception):
    pass


class Monitor(ABC):
    @abstractmethod
    def coletar_dados(self):
        raise MonitorError("Chame Monitor por meio de suas funções, ex: MonitorCPU")


class MonitorCPU(Monitor):
    def coletar_dados(self):
        return f"Uso de CPU: {psutil.cpu_percent(interval=1)}%"


class MonitorMemoria(Monitor):
    def coletar_dados(self):
        return f"Uso de memória: {psutil.virtual_memory().percent}%"


class MonitorDisco(Monitor):
    def coletar_dados(self):
        return f"Uso de disco: {psutil.disk_usage('/').percent}%"


def exibir_status(monitores):
    for monitor in monitores:
        print(monitor.coletar_dados())


if __name__ == "__main__":
    exibir_status([MonitorCPU(), MonitorMemoria(), MonitorDisco()])
