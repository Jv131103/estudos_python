class GerenciadorTarefas:
    def __init__(self) -> None:
        self.tarefas = []

    def adicionar(self, descricao):
        descricao = descricao.strip().lower()

        for tarefa in self.tarefas:
            if tarefa["descricao"] == descricao:
                return False  # já existe

        self.tarefas.append({
            "descricao": descricao,
            "concluida": False
        })
        return True

    def concluir_tarefa(self, descricao):
        descricao = descricao.strip().lower()

        for tarefa in self.tarefas:
            if tarefa["descricao"] == descricao:
                tarefa["concluida"] = True
                return True

        return False  # não encontrada

    def listar_tarefas(self) -> list[str]:
        resultado = []

        for tarefa in self.tarefas:
            status = "[x]" if tarefa["concluida"] else "[ ]"
            resultado.append(f"{status} {tarefa['descricao']}")

        return resultado


tarefas_do_jota = GerenciadorTarefas()
tarefas_do_jota.adicionar("Fazer Kumon")
tarefas_do_jota.adicionar("Estudar programação")
tarefas_do_jota.adicionar("Estudar audiobooks de filosofia")
tarefas_do_jota.adicionar("Ler a bíblia")
tarefas_do_jota.concluir_tarefa("Estudar programação")

for linha in tarefas_do_jota.listar_tarefas():
    print(linha)
