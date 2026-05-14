from sklearn.model_selection import train_test_split


"""
train_test_split:

    Treino:

        aprender

    Teste:

        prova surpresa

    Analogia:

        Você ensina uma criança:

            2+2 = 4
            3+3 = 6

        Depois testa:

            5+5 = ?

    Se acertar:

        aprendeu padrão.

        Se decorar:

            falha

    param random_state?

        Isso fixa embaralhamento.

        Sem:

            cada execução muda.

        Com:

            42

        resultado reproduzível.

    param test_size:

        significa:

            n% dos dados vão para TESTE

        e automaticamente:

            resto% vão para TREINO

        Visual mental

            Se você tem 10 linhas:

                [1]
                [2]
                [3]
                [4]
                [5]
                [6]
                [7]
                [8]
                [9]
                [10]

        com:

            test_size=0.2

        fica:

            treino (80%): 8 linhas

            teste (20%): 2 linhas

    Matemática

        É literalmente:

            10 * 0.2 = 2

        2 linhas no teste.

        Resto:

            10 - 2 = 8

        treino.

        Valores comuns:

            Muito usados:

                80/20

                test_size=0.2

                70/30

                    test_size=0.3

                Mais dados para testar.

                Menos treino.

                90/10

                    test_size=0.1

                Mais treino.

                Menos validação.
"""

import pandas as pd

df = pd.read_csv("./IA/regressao_linear/notas.csv")

X = df[["horas_estudo"]]
Y = df["nota"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

print(X_train)
