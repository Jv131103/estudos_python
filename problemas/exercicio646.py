"""
Crie uma classe abstrata Notificador
com método enviar()
e implemente Email e SMS.
"""

from abc import ABC, abstractmethod


class Notificador(ABC):
    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> None:
        pass


class Email(Notificador):
    def enviar(self):
        print("Enviando email...")
        print(self.mensagem)


class SMS(Notificador):
    def enviar(self):
        print("Enviando SMS...")
        print(self.mensagem)


def enviar_para(pessoa, notificador: Notificador):
    print(f"ENVIANDO PARA {pessoa}")
    notificador.enviar()


usuario = "DevTeste"
mensagem = "Olá, tudo bom?"

notificadores = [
    Email(mensagem),
    SMS(mensagem)
]

for n in notificadores:
    enviar_para(usuario, n)
