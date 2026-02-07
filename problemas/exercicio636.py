"""
Tema: Sistema de notificações

    Classes base

        EmailNotificador

            método enviar_email(mensagem)

        SMSNotificador

            método enviar_sms(mensagem)

    Classe de apoio (delegação)

        Logger

            método registrar(evento)

    Classe principal

        SistemaAlerta(EmailNotificador, SMSNotificador)

            recebe um Logger no construtor

            método enviar_alerta(mensagem) que:

                envia email

                envia sms

                registra no log (delegando ao Logger)

Regras importantes

    Não herdar de Logger

    Logger deve ser usado por delegação

    Herança múltipla só para comportamentos compatíveis

Pista mental

    Herança múltipla = capacidades
    Delegação = responsabilidade externa
"""


class EmailNotificador:
    def enviar_email(self, mensagem):
        return mensagem


class SMSNotificador:
    def enviar_sms(self, mensagem):
        return mensagem


class Logger:
    def registrar(self, evento):
        return f"[LOG] {evento}"


class SistemaAlerta(EmailNotificador, SMSNotificador):
    def __init__(self, logger: Logger) -> None:
        self.logger = logger  # delegação (injeção)

    def enviar_alerta(self, mensagem):
        print(self.enviar_email(mensagem))
        print(self.enviar_sms(mensagem))
        print(self.logger.registrar("Alerta enviado com sucesso"))


sistema = SistemaAlerta(Logger())
sistema.enviar_alerta("Atenção, isso é um teste não se preocupe")
