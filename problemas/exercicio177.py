import os

DIR_ARQUIVOS = os.path.join(os.getcwd(), "arquivos")
os.makedirs(DIR_ARQUIVOS, exist_ok=True)


def abrir_registro(arquivo=f"{DIR_ARQUIVOS}/notas.txt", encode="utf-8"):
    with open(arquivo, "r", encoding=encode) as arquivo:
        dados = arquivo.readlines()

        dados = [editado.replace("\n", "").replace(",", ".") for editado in dados]

        lista_informacao = []
        for dado in dados:
            nome, nota1, nota2, nota3 = dado.split(";")
            nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
            lista_informacao.append([nome, nota1, nota2, nota3])
        return lista_informacao


def escrever_registro(dados, arquivo=f"{DIR_ARQUIVOS}/resultado_notas.txt", encode="utf-8"):
    with open(arquivo, "w", encoding=encode) as arquivo:
        for dado in dados:
            arquivo.write(dado + "\n")


def retornar_resultado_notas(registro):
    lista_retornada = []
    for aluno in registro:
        nome, nota1, nota2, nota3 = aluno
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            status = "Aprovado"
        elif 5 <= media < 7:
            status = "Recuperação"
        else:
            status = "Reprovado"

        string = f"{nome};{media:.2f};{status}"

        lista_retornada.append(string)
    return lista_retornada


registro = abrir_registro()
dados = retornar_resultado_notas(registro)
escrever_registro(dados)
