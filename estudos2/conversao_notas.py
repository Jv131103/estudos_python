class StructManual:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        atributos = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({atributos})"


def avalicao_nota_final(nota_final):
    if not (0 <= nota_final <= 10):
        raise ValueError("Nota inválida, digite uma nota de 0 a 10")

    tabela_notas = [
        StructManual(nota_inicial=0.0, nota_final=5.0, conceito="F", situacao="Reprovado"),
        StructManual(nota_inicial=5.0, nota_final=7.0, conceito="D", situacao="Reprovado"),
        StructManual(nota_inicial=7.0, nota_final=8.0, conceito="C", situacao="Aprovado"),
        StructManual(nota_inicial=8.0, nota_final=9.0, conceito="B", situacao="Aprovado"),
        StructManual(nota_inicial=9.0, nota_final=10, conceito="A", situacao="Aprovado com louvor"),
    ]

    for notas in tabela_notas:
        if notas.nota_final == 10:  # última faixa, fecha os dois lados
            condicao = notas.nota_inicial <= nota_final <= notas.nota_final
        else:
            condicao = notas.nota_inicial <= nota_final < notas.nota_final

        if condicao:
            print(f"Nota: {nota_final:.2f}")
            print(f"Retorno: {notas.conceito} | Status: {notas.situacao}")
            break
    else:
        print("NOTA FORA DO INTERVALO")

    print()
    print("--" * 30)


def trata_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite apenas números")
            print()
            continue


def trata_msg(msg, tipo):
    while True:
        valor = input(msg).lower().replace("ã", 'a').strip()
        if not valor:
            print(f"Não digite mensagens vazias para {tipo}!")
            print()
            continue
        elif valor not in ["sim", 'nao']:
            print("Digite apenas Sim ou Não!")
            print()
            continue
        return valor


def main():
    while True:
        try:
            print("==" * 30)
            nota = trata_float("Nota do aluno: ")

            avalicao_nota_final(nota)

            nova_consulta = trata_msg("Nova nota? [SIM | NAO] ", "NOVA_CONSULTA")
            if nova_consulta == 'nao':
                break
        except ValueError as ve:
            print(ve)
            print()


main()
