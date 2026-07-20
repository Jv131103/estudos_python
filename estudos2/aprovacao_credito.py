def aprova_credito_versionIF(score, renda, cliente_antigo=None):
    tem_renda = (renda == "sim")
    e_antigo = (cliente_antigo == "sim")

    if score >= 700 and tem_renda:
        return 'Aprovado, limite alto'
    elif score >= 700 and not tem_renda and e_antigo:
        return 'Aprovado, limite médio'
    elif score >= 700 and not tem_renda and not e_antigo:
        return "Aprovado, limite baixo"
    elif 500 <= score <= 699 and tem_renda and e_antigo:
        return 'Aprovado, limite médio'
    elif 500 <= score <= 699 and tem_renda and not e_antigo:
        return 'Aprovado, limite baixo'
    elif 500 <= score <= 699 and not tem_renda:
        return 'Negado, sugerir cartão consignado'

    else:
        return "Negado"


def aprova_credito_match(score: int, renda_alta: str, cliente_antigo: str) -> str:
    tem_renda = (renda_alta == "sim")
    e_antigo = (cliente_antigo == "sim")

    match score:
        case s if s >= 700 and tem_renda:
            return 'Aprovado, limite alto'
        case s if s >= 700 and not tem_renda and e_antigo:
            return 'Aprovado, limite médio'
        case s if s >= 700 and not tem_renda and not e_antigo:
            return 'Aprovado, limite baixo'
        case s if 500 <= s <= 699 and tem_renda and e_antigo:
            return 'Aprovado, limite médio'
        case s if 500 <= s <= 699 and tem_renda and not e_antigo:
            return 'Aprovado, limite baixo'
        case s if 500 <= s <= 699 and not tem_renda:
            return 'Negado, sugerir cartão consignado'
        case _:
            return 'Negado'


from dataclasses import dataclass
from typing import Optional


@dataclass
class RegraCredito:
    score_min: int
    score_max: int
    renda_alta: Optional[bool]      # True = Sim, False = Não, None = Tanto faz (—)
    cliente_antigo: Optional[bool]  # True = Sim, False = Não, None = Tanto faz (—)
    resultado: str


def aprova_credito_motor(score: int, renda_input: str, cliente_input: str) -> str:
    # 1. Normaliza as entradas para Booleanos
    tem_renda = True if renda_input == "sim" else False
    e_antigo = True if cliente_input == "sim" else False

    # 2. Define a matriz de regras exatamente como a tabela do enunciado
    tabela_regras = [
        RegraCredito(700, 1000, True, None, "Aprovado, limite alto"),
        RegraCredito(700, 1000, False, True, "Aprovado, limite médio"),
        RegraCredito(700, 1000, False, False, "Aprovado, limite baixo"),
        RegraCredito(500, 699, True, True, "Aprovado, limite médio"),
        RegraCredito(500, 699, True, False, "Aprovado, limite baixo"),
        RegraCredito(500, 699, False, None, "Negado, sugerir cartão consignado"),
        RegraCredito(0, 499, None, None, "Negado")
    ]

    # 3. O "Motor" avalia linha por linha
    for regra in tabela_regras:
        # Valida faixa de score
        if not (regra.score_min <= score <= regra.score_max):
            continue

        # Valida renda (se a regra exigir um valor específico)
        if regra.renda_alta is not None and regra.renda_alta != tem_renda:
            continue

        # Valida tempo de casa (se a regra exigir um valor específico)
        if regra.cliente_antigo is not None and regra.cliente_antigo != e_antigo:
            continue

        # Se passou por todos os filtros da linha, encontramos a regra correspondente
        return regra.resultado

    return "Negado"  # Fallback de segurança


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def trata_msg(msg):
    while True:
        valor = input(msg).lower().replace("ã", 'a').strip()
        if not valor:
            print("Não digite valores vazios")
            continue
        return valor


def sistema_aprovacao():
    while True:
        score = trata_int("Score do cliente: ")
        renda = trata_msg("Cliente têm renda >= 3000? [sim, nao] ")
        cliente_antigo = trata_msg("O cliente têm mais de 2 anos de casa? [sim, nao] ")

        retorno = aprova_credito_versionIF(score, renda, cliente_antigo)
        retorno2 = aprova_credito_match(score, renda, cliente_antigo)
        retorno3 = aprova_credito_motor(score, renda, cliente_antigo)

        print("Retorno para o cliente:")
        print("\t", end="")
        print("==" * 20)
        print(f"\tScore: {score}")
        print(f"\tRenda maior ou igual a R$ 3000,00: {renda}")
        print(f"\tCliente há +2 anos: {cliente_antigo}")
        print("\t", end="")
        print("--" * 20)
        print(f"\tRetorno ao cliente versao IF: {retorno}")
        print(f"\tRetorno ao cliente versao MATCH: {retorno2}")
        print(f"\tRetorno ao cliente versao MOTOR: {retorno3}")
        print("\t", end="")
        print("--" * 20)

        print()
        de_novo = trata_msg("Nova consulta? [sim, nao] ")
        if de_novo == "nao":
            print("Encerrando o sistema...")
            break


sistema_aprovacao()
