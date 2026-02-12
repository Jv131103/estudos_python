from abc import ABC, abstractmethod


# Interfaces
class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem: str):
        pass


# Implementações
class Email(Notificador):
    def notificar(self, mensagem: str):
        print(f"Notificando EMAIL: {mensagem}")


class SMS(Notificador):
    def notificar(self, mensagem: str):
        print(f"Notificando SMS: {mensagem}")


# Managers
class NotificadorManager:
    _envios = {"email": Email, "sms": SMS}

    @classmethod
    def criar(cls, tipo: str) -> Notificador:
        classe = cls._envios.get(tipo)
        if not classe:
            raise ValueError("Tipo inválido")
        return classe()

    @classmethod
    def enviar(cls, tipo: str, mensagem: str) -> None:
        cls.criar(tipo).notificar(mensagem)


# setups
def setup_notificador_email():
    NotificadorManager.enviar("email", "Olá mundo")


def setup_notificador_sms():
    NotificadorManager.enviar("sms", "Olá mundo")


# Execução
setup_notificador_email()
setup_notificador_sms()
