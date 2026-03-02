"""
Observando o mercado de educação infantil, você e sua equipe decidem
desenvolver um aplicativo para que as crianças aprendam a como controlar
os seus gastos.

Para validar o protótipo, foi solicitado que você elabore um script simples,
onde o usuário deverá informar quantas transações financeiras realizou ao
longo de um dia e, na sequência, deverá informar o valor de cada uma das
transações que realizou.

No final, seu programa precisa exibir o valor total dos gastos realizados
pelo usuário, assim como a média do valor de cada transação.
"""


def main():
    try:
        qtd_transacoes = int(input("Quantidade de transações ao dia: "))
        if qtd_transacoes <= 0:
            print("Sem transações no dia!")
            return

        total = 0
        for i in range(1, qtd_transacoes + 1):
            while True:
                try:
                    valor = float(input(f"Gasto na transação {i}: ").replace(",", "."))
                    if valor < 0:
                        print("Valor não pode ser negativo.")
                        continue
                    total += valor
                    break
                except ValueError:
                    print("Digite apenas números válidos.")

        media_gastos = total / qtd_transacoes

        print(f"Gasto total: R$ {total:.2f}")
        print(f"Média de gastos: R$ {media_gastos:.2f}")
    except ValueError:
        print("Digite apenas números inteiros")


main()
