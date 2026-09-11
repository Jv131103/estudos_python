class Funcionario:
    def __init__(self, nome, senioridade) -> None:
        self.nome = nome.title()
        self.senioridade = senioridade.lower()


def calcular_bonus(funcionario):
    tabela_bonus = {
        "junior": 500,
        "pleno": 1000,
        "senior": 2000
    }

    return tabela_bonus.get(funcionario.senioridade, 0.00)


def funcionario_com_maior_bonus(lista_funcionarios):
    campeao = None
    maior_bonus = -1

    for funcionario in lista_funcionarios:
        bonus = calcular_bonus(funcionario)
        if bonus > maior_bonus:
            campeao = funcionario
            maior_bonus = bonus

    return {"nome": campeao.nome, "senioridade": campeao.senioridade, "bonus": maior_bonus}


funcionarios = [
    Funcionario("Irineu", "junior"),
    Funcionario("Matias", "junior"),
    Funcionario("Lucas", "pleno"),
    Funcionario("João", "Senior"),
    Funcionario("Renato", "senior"),
]

print(funcionario_com_maior_bonus(funcionarios))
