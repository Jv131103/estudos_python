"""
CofreDigital com tentativa limitada + bloqueio + logs internos

Implementação seguindo exatamente os requisitos:
- estado interno protegido
- API mínima
- bloqueio após 3 erros
- logs internos sem “vazar” lista original
"""


class CofreDigital:
    def __init__(self, segredo: str, pin: str) -> None:
        self._segredo = str(segredo)
        self._pin = self._validar_pin(pin)  # garante pin numérico e tamanho ok
        self._tentativas = 0
        self._bloqueado = False
        self._log = []

        self._registrar_log("Cofre criado")

    # --------- utilitários internos ---------
    def _registrar_log(self, evento: str) -> None:
        self._log.append(evento)

    def _validar_pin(self, pin: str) -> str:
        if not isinstance(pin, str):
            raise ValueError("PIN deve ser string")
        if not pin.isdigit():
            raise ValueError("PIN deve conter apenas dígitos")
        if not (4 <= len(pin) <= 8):
            raise ValueError("PIN deve ter de 4 a 8 dígitos")
        return pin

    def _checar_pin(self, pin: str) -> bool:
        return isinstance(pin, str) and pin == self._pin

    # --------- API pública ---------
    @property
    def status(self) -> dict:
        # somente leitura; devolve um dict novo
        return {"bloqueado": self._bloqueado, "tentativas": self._tentativas}

    def abrir(self, pin: str) -> str:
        if self._bloqueado:
            self._registrar_log("Tentativa de abrir com cofre bloqueado")
            raise PermissionError("Cofre bloqueado")

        if not self._checar_pin(pin):
            self._tentativas += 1
            self._registrar_log(f"PIN incorreto (tentativa {self._tentativas})")

            if self._tentativas >= 3:
                self._bloqueado = True
                self._registrar_log("Cofre bloqueado após 3 tentativas inválidas")

            raise ValueError("PIN incorreto")

        # pin correto
        self._tentativas = 0
        self._registrar_log("Cofre aberto com sucesso")
        return self._segredo

    def resetar(self, pin_atual: str, novo_pin: str) -> None:
        if self._bloqueado:
            self._registrar_log("Tentativa de resetar com cofre bloqueado")
            raise PermissionError("Cofre bloqueado")

        if not self._checar_pin(pin_atual):
            self._registrar_log("Reset falhou: PIN atual incorreto")
            raise ValueError("PIN atual incorreto")

        novo_pin_validado = self._validar_pin(novo_pin)
        self._pin = novo_pin_validado
        self._tentativas = 0
        self._registrar_log("PIN resetado com sucesso")

    def ver_log(self, pin: str) -> list:
        if not self._checar_pin(pin):
            self._registrar_log("Acesso ao log negado (PIN incorreto)")
            raise PermissionError("Acesso negado")
        self._registrar_log("Log acessado")
        return list(self._log)  # cópia, não vaza a lista original


# --------- Teste rápido (opcional) ---------
if __name__ == "__main__":
    cofre = CofreDigital(segredo="MEU SEGREDO", pin="1234")

    # 2 erros
    for tentativa in ["0000", "1111"]:
        try:
            cofre.abrir(tentativa)
        except Exception as e:
            print("ERRO:", e)

    print("STATUS:", cofre.status)  # tentativas = 2

    # 3º erro -> bloqueia
    try:
        cofre.abrir("2222")
    except Exception as e:
        print("ERRO:", e)

    print("STATUS:", cofre.status)  # bloqueado = True

    # tentar abrir bloqueado
    try:
        cofre.abrir("1234")
    except Exception as e:
        print("ERRO:", e)

    # ver log com PIN correto (vai falhar pois bloqueado não impede ver_log; requisito não proíbe)
    try:
        print("LOG (cópia):", cofre.ver_log("1234"))
    except Exception as e:
        print("ERRO:", e)
