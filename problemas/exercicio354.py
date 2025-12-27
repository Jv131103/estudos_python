class SessaoUsuario:
    def __init__(self, usuario) -> None:
        self.usuario = usuario
        self.logado = False
        self.tentativas = 0

    def ja_esta_logado(self):
        return self.logado

    def login(self, senha):
        if self.ja_esta_logado():
            print("Usuário já logado")
            return self.logado

        if self.tentativas == 3:
            print("Usuário encontra-se bloqueado no momento")
            return self.logado

        if senha == "1234":
            self.logado = True
        else:
            print("Senha inválida")
            self.tentativas += 1

        return self.logado

    def logout(self):
        if not self.ja_esta_logado():
            print("Usuário já deslogado")
            return self.logado

        self.logado = False
        return self.logado

    def status(self):
        saida_logado = 'Sim' if self.ja_esta_logado() else 'Não'
        saida_bloqueio = 'Sim' if self.tentativas >= 3 else 'Não'
        print(f"Usuário: {self.usuario} | Logado: {saida_logado} | Bloqueado: {saida_bloqueio}")


usuario_joao = SessaoUsuario("JOÃO")
usuario_joao.logout()
usuario_joao.status()
usuario_joao.login("batata")
usuario_joao.login("batata")
usuario_joao.login("batata")
usuario_joao.status()
usuario_joao.login("1234")
print()
usuario_renato = SessaoUsuario("RENATO")
usuario_renato.login("1234")
usuario_renato.status()
usuario_renato.logout()
usuario_renato.status()
