import csv
import os
from pathlib import Path

bucket_alunos = []


def pedir_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números inteiros.")


def pedir_nota_de_0_a_10(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))
            if not (0 <= nota <= 10):
                print("Digite uma nota no intervalo de 0 a 10")
                continue
            return nota
        except ValueError:
            print("Digite apenas números decimais.")


def pedir_nome(mensagem):
    while True:
        nome = input(mensagem).strip().title()
        if not nome:
            print("Nome não pode ser vazio!")
            continue
        return nome


def calcular_media(nota1, nota2):
    return round((nota1 + nota2) / 2, 2)


def cadastrar():
    aluno = {}
    aluno["nome"] = pedir_nome("Nome do aluno: ")
    aluno["idade"] = pedir_inteiro("Idade: ")
    aluno["nota1"] = pedir_nota_de_0_a_10("Nota 1: ")
    aluno["nota2"] = pedir_nota_de_0_a_10("Nota 2: ")
    aluno["media"] = calcular_media(aluno["nota1"], aluno["nota2"])
    bucket_alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucesso!")
    print()


def listar():
    if not bucket_alunos:
        print("Nenhum aluno cadastrado.")
        print()
        return

    for idx, aluno in enumerate(bucket_alunos):
        print(f"{idx} - {aluno['nome']}")
    print()


def atualizar():
    if not bucket_alunos:
        print("Nenhum aluno cadastrado.")
        print()
        return

    listar()
    indice = pedir_inteiro(f"Digite o id do aluno de 0 até {len(bucket_alunos) - 1}: ")
    if indice < 0 or indice >= len(bucket_alunos):
        print("Aluno não encontrado")
        print()
        return

    aluno = bucket_alunos[indice]
    aluno["nome"] = pedir_nome("Nome do aluno: ")
    aluno["idade"] = pedir_inteiro("Idade: ")
    aluno["nota1"] = pedir_nota_de_0_a_10("Nota 1: ")
    aluno["nota2"] = pedir_nota_de_0_a_10("Nota 2: ")
    aluno["media"] = calcular_media(aluno["nota1"], aluno["nota2"])
    print(f"Aluno {aluno['nome']} atualizado com sucesso!")
    print()


def remover():
    if not bucket_alunos:
        print("Nenhum aluno cadastrado.")
        print()
        return

    listar()
    indice = pedir_inteiro(f"Digite o id do aluno de 0 até {len(bucket_alunos) - 1}: ")
    if indice < 0 or indice >= len(bucket_alunos):
        print("Aluno não encontrado")
        print()
        return

    dados = bucket_alunos.pop(indice)
    print(f"Aluno {dados['nome']} removido com sucesso")
    print()
    return dados


def media():
    if not bucket_alunos:
        print("Nenhum aluno cadastrado.")
        print()
        return

    for idx, aluno in enumerate(bucket_alunos):
        media = aluno['media']
        resposta = "aprovado" if media >= 7 else "reprovado"
        print(f"Aluno {idx} -> Média: {media:.2f} -> {resposta}")
    print()


def media_aluno():
    if not bucket_alunos:
        print("Nenhum aluno cadastrado.")
        print()
        return

    listar()
    indice = pedir_inteiro("Digite o id do aluno: ")
    if indice < 0 or indice >= len(bucket_alunos):
        print("Aluno não encontrado")
        print()
        return

    aluno = bucket_alunos[indice]
    media = aluno["media"]
    resposta = "aprovado" if media >= 7 else "reprovado"
    print(f"Aluno {indice} -> Média: {media:.2f} -> {resposta}")
    print()


def sair():
    print("Encerrando o programa!")


def salvar_csv():
    try:
        if not bucket_alunos:
            print("Não há alunos para registrar!")
            print()
            return

        pasta = Path("./csvs")
        pasta.mkdir(exist_ok=True)

        arquivo = pasta / "notas_alunos.csv"
        with open(arquivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=bucket_alunos[0].keys())

            writer.writeheader()   # escreve o cabeçalho
            writer.writerows(bucket_alunos)  # escreve os dados

        print(f"CSV salvo com sucesso em {arquivo}!")
    except Exception as e:
        print(f"CSV não salvo! Motivo: {e}")


def carregar_csv():
    try:
        arquivo = Path("./csvs/notas_alunos.csv")
        if not arquivo.exists():
            return

        bucket_alunos.clear()

        with open(arquivo, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for linha in reader:
                bucket_alunos.append({
                    "nome": linha["nome"],
                    "idade": int(linha["idade"]),
                    "nota1": float(linha["nota1"]),
                    "nota2": float(linha["nota2"]),
                    "media": float(linha["media"])
                })

        print("Dados carregados com sucesso!")
        print()

    except Exception as e:
        print(f"Erro ao carregar CSV: {e}")


options = [
    ["1", "Cadastrar aluno", cadastrar],
    ["2", "Listar alunos", listar],
    ["3", "Atualizar aluno", atualizar],
    ["4", "Remover aluno", remover],
    ["5", "Ver média dos alunos", media],
    ["6", "Ver média de um aluno", media_aluno],
    ["7", "Salvar bucket em CSV", salvar_csv]
]

carregar_csv()

while True:
    print("------ TABELA DE ALUNOS ------")
    for opc, tipo, _ in options:
        print(f"{opc} - {tipo}")
    print("8 - SAIR")
    print()

    escolha = input("Opção: ")
    os.system("cls" if os.name == "nt" else "clear")
    print()
    if escolha == '8':
        sair()
        break

    for opc, _, funcao in options:
        if opc == escolha:
            funcao()
            break
    else:
        print("Opção inválida, digite de 1 a 8")
        print()
