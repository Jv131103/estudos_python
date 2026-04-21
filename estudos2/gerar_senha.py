import secrets
import string

ESPECIAIS = "!@#$%&*+-_=?"
AMBIGUOS = "O0l1I"


def remover_ambiguos(texto):
    return "".join(c for c in texto if c not in AMBIGUOS)


def gerar_senha(
    tamanho=10,
    usar_maiusculas=True,
    usar_minusculas=True,
    usar_numeros=True,
    usar_especiais=True,
    evitar_ambiguos=False
):
    grupos = []

    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)

    if usar_minusculas:
        grupos.append(string.ascii_lowercase)

    if usar_numeros:
        grupos.append(string.digits)

    if usar_especiais:
        grupos.append(ESPECIAIS)

    if not grupos:
        raise ValueError("Pelo menos um grupo de caracteres deve ser ativado")

    if evitar_ambiguos:
        grupos = [remover_ambiguos(grupo) for grupo in grupos]
        grupos = [grupo for grupo in grupos if grupo]

    if tamanho < len(grupos):
        raise ValueError(
            f"A senha precisa ter pelo menos {len(grupos)} caracteres "
            f"para incluir todos os grupos obrigatórios"
        )

    senha = []

    # garante pelo menos 1 de cada grupo
    for grupo in grupos:
        senha.append(secrets.choice(grupo))

    # conjunto total para completar o resto
    todos = "".join(grupos)

    while len(senha) < tamanho:
        senha.append(secrets.choice(todos))

    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)


print(gerar_senha(8))
