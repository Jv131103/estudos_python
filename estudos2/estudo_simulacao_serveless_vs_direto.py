import time

# ==============================================================================
# CONFIGURAÇÃO
# Altere o valor de MODO para mudar o comportamento:
#  - "SEMPRE_ATIVO" : Roda em loop contínuo consumindo recursos no tempo ocioso.
#  - "SO_QUANDO_CHAMADO" : Fica "adormecido" e executa apenas ao receber um evento.
# ==============================================================================
# ==============================================================================
# COMPARATIVO DAS ABORDAGENS (NUVEM / AWS)
# ==============================================================================
"""
+---------------------+---------------------------------------------------------+-------------------------------------------------------------+
| CARACTERÍSTICA      | RODAR SEM PARAR (SEMPRE ATIVO / EC2)                    | RODAR AO SER CHAMADO (SERVERLESS / LAMBDA)                 |
+---------------------+---------------------------------------------------------+-------------------------------------------------------------+
| Cobrança            | Paga pelo tempo que a máquina fica ligada (mesmo ociosa)| Paga estritamente pelo número de requisições e tempo de exec|
| Tempo de Resposta   | Resposta imediata (baixa latência constante)            | Pode ter uma pequena latência inicial (Cold Start)          |
| Escalabilidade      | Exige configurar balanceadores e servidores manualmente  | Escala automaticamente de 0 para milhares em paralelo       |
| Ideal para          | Sistemas com tráfego constante de requisições por seg.  | APIs com picos, rotinas esporádicas ou arquivos             |
+---------------------+---------------------------------------------------------+-------------------------------------------------------------+
"""

MODO = "SO_QUANDO_CHAMADO"  # Altere para "SEMPRE_ATIVO" para testar o outro modo

# Fila simulada de chamadas/requisições recebidas
requisicoes_recebidas = ["Processar Pedido #101", "Processar Pedido #102"]


# 1. TÉCNICA 1: Sempre Ativo (Modelo Servidor Contínuo / EC2)
def executar_modo_sempre_ativo():
    print("\n--- [MODO SEMPRE ATIVO INICIADO] ---")
    print("O servidor está rodando 24/7 e consumindo recursos constantemente...")

    ciclos_ociosos = 0
    # O servidor roda em um loop infinito monitorando se há trabalho
    while ciclos_ociosos < 3:
        if requisicoes_recebidas:
            tarefa = requisicoes_recebidas.pop(0)
            print(f"[EXECUTANDO] Processando: '{tarefa}'")
        else:
            ciclos_ociosos += 1
            print(
                f"[OCIOSO] Nenhuma chamada recebida. O servidor continua ligado e gastando... (Ciclo {ciclos_ociosos})"
            )

        time.sleep(1)

    print("--- [SIMULAÇÃO ENCERRADA] ---\n")


# 2. TÉCNICA 2: Apenas quando chamado (Modelo Serverless / AWS Lambda)
def tratar_evento(evento):
    """Esta função só é instanciada e executada quando um evento chega."""
    print(f"[EXECUTANDO] Evento recebido! Processando: '{evento}'")
    # Executa a lógica rápida e "desliga" / encerra a execução
    print("[FINALIZADO] Função concluída. Retornando ao estado adormecido.")


def executar_modo_so_quando_chamado():
    print("\n--- [MODO SERVERLESS / SÓ QUANDO CHAMADO INICIADO] ---")
    print("O código está 100% adormecido. Custo e consumo de CPU = 0.")

    # O código não roda nada até que a lista de requisições simule a chegada de um evento
    while requisicoes_recebidas:
        time.sleep(1)  # Simula a chegada do evento
        evento_atual = requisicoes_recebidas.pop(0)

        # Dispara a função pontualmente (Gatilho/Trigger)
        tratar_evento(evento_atual)

    print(
        "[ADORMECIDO] Nenhuma chamada ativa. O código não consome nenhum recurso."
    )
    print("--- [SIMULAÇÃO ENCERRADA] ---\n")


# EXECUÇÃO DO PROGRAMA
if __name__ == "__main__":
    if MODO == "SEMPRE_ATIVO":
        executar_modo_sempre_ativo()
    elif MODO == "SO_QUANDO_CHAMADO":
        executar_modo_so_quando_chamado()
    else:
        print("Modo inválido. Escolha 'SEMPRE_ATIVO' ou 'SO_QUANDO_CHAMADO'.")
