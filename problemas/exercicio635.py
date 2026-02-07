"""
Crie:

dois mixins (LogMixin, NotificacaoMixin)

uma classe que use ambos
"""


class LogMixin:
    def log(self, msg):
        print(f"[LOG] {msg}")


class NotificacaoMixin:
    def notificacao(self, msg):
        print(f"[NOTIFICACAO] {msg}")


class StatusmLog(LogMixin, NotificacaoMixin):
    def executar_log(self, msg):
        self.log(msg)

    def executar_notificacao(self, msg):
        self.notificacao(msg)


status = StatusmLog()
status.executar_log("INICIANDO LOG")
status.executar_notificacao("INICIANDO NOTIFICACAO")
