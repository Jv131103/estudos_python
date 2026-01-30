"""
Faça um programa que:

    Abra um arquivo saida.txt em modo escrita

    Escreva várias mensagens simulando um log

    Use flush() após algumas escritas

    Explique (comentário) por que o flush foi usado

DICAS

    write() não grava imediatamente

    flush() força escrita no SO

    Use comentários para explicar
"""


def gerar_saida_rapida(*messages, arquivo, flush_in=3):
    with open(arquivo, "w", encoding="utf-8") as file:
        cont = 0
        for message in messages:
            file.write(f"{message}\n")

            if cont == flush_in:
                file.flush()  # Utilizado para entrda rápida sem necessidade de buffer
                cont = -1

            cont += 1


gerar_saida_rapida(
    "[LOG] CRIANDO",
    "[TEST] ADICIONANDO TEXTO 1",
    "[TEST] ADICIONANDO TEXTO 2",
    "[TEST] ADICIONANDO TEXTO 3",
    "[TEST] ADICIONANDO TEXTO 4",
    "[TEST] ADICIONANDO TEXTO 5",
    "[TEST] ADICIONANDO TEXTO 6",
    "[TEST] ADICIONANDO TEXTO 7",
    "[TEST] ADICIONANDO TEXTO 8",
    "[ENDLOG] FIM DA GERAÇÃO DE LOG",
    arquivo="./arquivos/saida.txt"
)
