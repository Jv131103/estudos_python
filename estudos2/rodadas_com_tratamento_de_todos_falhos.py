import random


def passo_1():
    print("Executando passo 1...")
    if random.random() < 0.3:  # simula falha aleatória
        raise ValueError("Falha no passo 1")
    print("Passo 1 concluído com sucesso!")


def passo_2():
    print("Executando passo 2...")
    if random.random() < 0.3:
        raise ValueError("Falha no passo 2")
    print("Passo 2 concluído com sucesso!")


def passo_3():
    print("Executando passo 3...")
    if random.random() < 0.3:
        raise ValueError("Falha no passo 3")
    print("Passo 3 concluído com sucesso!")


# Lista de passos na ordem que devem ser executados
passos = [passo_1, passo_2, passo_3]


rodada = 1
todos_ok = False

while not todos_ok and rodada <= 10:
    print(f"\n=== Rodada {rodada} ===")
    resultados = []

    for i, passo in enumerate(passos, start=1):
        try:
            passo()
            resultados.append(True)
        except Exception as e:
            print(f"⚠️ Passo {i} falhou: {e}")
            resultados.append(False)

    todos_ok = all(resultados)
    rodada += 1

if todos_ok:
    print("\n✅ Todos os passos concluídos com sucesso!")
else:
    print("\n❌ Número máximo de rodadas atingido sem sucesso total.")
