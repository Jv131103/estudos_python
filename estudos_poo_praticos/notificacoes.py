from abc import ABC, abstractmethod


class CanalNotificacao(ABC):
    @abstractmethod
    def enviar(self, msg: str) -> None:
        """Toda subclasse concreta deve implementar o envio da mensagem."""
        pass


class Email(CanalNotificacao):
    def enviar(self, msg: str) -> str:
        return f"[EMAIL] enviado: {msg}"


class SMS(CanalNotificacao):
    def enviar(self, msg: str) -> str:
        return f"[SMS] enviado: {msg}"


class Push(CanalNotificacao):
    def enviar(self, msg: str) -> str:
        return f"[PUSH] enviado: {msg}"


class Usuario:
    def __init__(self, nome: str, canais: None | list = None) -> None:
        self.nome = nome
        self.canais = canais if canais is not None else []


class SistemaNotificacao:
    def notificar(self, usuario: Usuario, msg: str):
        canais = usuario.canais

        for canal in canais:
            print(canal.enviar(msg))


usuario = Usuario("Ana", canais=[Email(), SMS()])
sistema = SistemaNotificacao()
sistema.notificar(usuario, "Seu pedido foi enviado!")

try:
    canal = CanalNotificacao()
except TypeError:
    print("Não se pode instanciar classe abstrata diretamente por conta que ela é uma classe modelo e padronizante para outras classes")
