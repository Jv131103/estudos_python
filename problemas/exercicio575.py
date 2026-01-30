"""
Criar seu próprio with

Faça um programa que:

    Crie uma classe ArquivoSeguro

    No __enter__:

        abra um arquivo

    No __exit__:

        feche o arquivo

    mostre uma mensagem indicando fechamento

    Use essa classe com with para escrever em um arquivo

DICAS

    Implemente __enter__ e __exit__

    Retorne o arquivo no __enter__

    Não use open fora do contexto
"""


class ArquivoSeguro:
    def __init__(self, name_file, mode="w", flush=False) -> None:
        self.name_file = name_file
        self.mode = mode
        self.file = None
        self.flush = flush

    def __enter__(self):
        try:
            print(f"Acessando arquivo no modo {self.mode}")
            self.file = open(self.name_file, self.mode)
            return self.file
        except Exception as e:
            print(f"Erro gerado ao acessar arquivo: {e}")
            return False

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file is None:
                print("ARQUIVO NÃO GERADO")
                return

            print("Fechando arquivo...")
            self.file.close()
            self.file = None
            return True
        except Exception as e:
            print(f"Erro ao fechar arquivo: {e}")
            return False

    def add_content(self, message="SEM MENSSAGEM"):
        if self.mode not in ["r", "rb"] and self.file is not None:
            self.file.write(f"{message}\n")
            if self.flush:
                self.file.flush()
            return True
        return False


if __name__ == "__main__":
    with ArquivoSeguro("teste1.py", flush=True) as file:
        file.add_content(  # type: ignore
            "print('OLÁ MUNDO, ESSE TEXTO FOI GERADO VIA MANAGER')"
        )
