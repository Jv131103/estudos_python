from datetime import datetime


class ArquivoLog:
    def __init__(self, caminho):
        self.caminho = caminho

    def registrar(self, mensagem):
        agora = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")
        with open(self.caminho, "a", encoding="utf-8") as arquivo:
            arquivo.writelines(f"{agora} {mensagem}\n")

    def ler(self):
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            return [linha.strip() for linha in arquivo]

    def limpar(self):
        with open(self.caminho, "w", encoding="utf-8"):
            return


log = ArquivoLog("./arquivos/registro.txt")
log.registrar("Sistema iniciado")
log.registrar("Erro: conexão perdida")
print(log.ler())
log.limpar()
print(log.ler())
