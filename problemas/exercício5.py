"""
Faça um programa para leitura de duas notas parciais de um aluno. O
programa deve calcular a média alcançada por um aluno e apresentar:

    . A mensagem "Aprovado", se a média alcançada for maior ou ugual asete;
    . A mensagem "Reprovado", se a média for menor do que sete;
    . A mensagem "Aprovado com Distinção", se a média for igual a dez;
"""

nota1 = float(input("Nota 1 do aluno: ").replace(",", "."))
nota2 = float(input("Nota 2 do aluno: ").replace(",", "."))

media = (nota1 + nota2) / 2

if abs(media) == 10:
    print("Aprovado com Distinção")
elif 7 <= media <= 9:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Valor inválido. As notas devem ser entre 0 e 10.")
