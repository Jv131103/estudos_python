import sqlite3
from pathlib import Path

Path("./databases").mkdir(parents=True, exist_ok=True)


class BancoCadastro:
    def __init__(self) -> None:
        self.conexao = sqlite3.connect("./databases/produtos.db")
        self.cursor = self.conexao.cursor()

    def create_table(self):
        try:
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT UNIQUE NOT NULL,
                    categoria TEXT NOT NULL,
                    qtd INTEGER DEFAULT 0,
                    preco REAL DEFAULT 0.00
                )
                '''
            )

            self.conexao.commit()
            print("✅ Banco criado ou já existe")
        except sqlite3.Error as e:
            print("❌ Erro ao criar tabela! Fechando por segurança...")
            print(f"Motivo: {e}")
            self.conexao.rollback()

    def create(self, nome, categoria, qtd, preco):
        try:
            nome = nome.title().strip()
            categoria = categoria.title().strip()
            self.cursor.execute(
                "INSERT INTO produtos(nome, categoria, qtd, preco) VALUES (?, ?, ?, ?)",
                (nome, categoria, qtd, preco)
            )
            self.conexao.commit()
            print("✅ Produto cadastrado!")
        except sqlite3.IntegrityError:
            print("❌ Produto com esse nome já cadastrado!")
        except sqlite3.Error as e:
            print(f"❌ Erro ao cadastrar dados: {e}")
            self.conexao.rollback()
        except Exception as e:
            print(f"❌ Excessão ocorrida: {e}")

    def read(self):
        try:
            self.cursor.execute("SELECT * FROM produtos")

            dados = self.cursor.fetchall()

            print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {'Qtd':<5} {'Preço':<10}")
            print("-" * 60)

            for id_, nome, categoria, qtd, preco in dados:
                print(f"{id_:<5} {nome:<20} {categoria:<15} {qtd:<5} R$ {preco:<10.2f}")
        except sqlite3.Error as e:
            print(f"❌ Erro ao listar dados: {e}")
            self.conexao.rollback()

    def update_qtd(self, id, new_qtd):
        try:
            self.cursor.execute(
                """
                UPDATE produtos
                SET qtd = ?
                WHERE id = ?
                """,
                (new_qtd, id)
            )

            self.conexao.commit()

            print(f"{self.cursor.rowcount} registro(s) atualizado(s).")

        except sqlite3.Error as e:
            print(f"❌ Erro ao atualizar: {e}")
            self.conexao.rollback()

    def delete(self, id):
        try:
            self.cursor.execute(
                """
                DELETE FROM produtos
                WHERE id = ?
                """,
                (id,)
            )

            self.conexao.commit()

            if self.cursor.rowcount:
                print("Produto removido com sucesso!")
                return
            else:
                print("❌ Produto não encontrado.")

        except sqlite3.Error as e:
            print(f"❌ Erro ao deletar: {e}")
            self.conexao.rollback()

    def buscar_por_categoria(self, categoria):
        try:
            self.cursor.execute(
                """
                SELECT id, nome, categoria, qtd, preco
                FROM produtos
                WHERE categoria = ?
                """,
                (categoria,)
            )

            produtos = self.cursor.fetchall()

            if produtos:
                for id_, nome, categoria, qtd, preco in produtos:
                    print(f"{id_:<5} {nome:<20} {categoria:<15} {qtd:<5} R$ {preco:<10.2f}")
            else:
                print("Nenhum produto encontrado nessa categoria.")

        except sqlite3.Error as e:
            print(f"Erro ao buscar categoria: {e}")

    def alerta_estoque_baixo(self, limite=5):
        try:
            self.cursor.execute(
                """
                SELECT id, nome, categoria, qtd, preco
                FROM produtos
                WHERE qtd <= ?
                ORDER BY qtd ASC
                """,
                (limite,)
            )

            produtos = self.cursor.fetchall()

            if produtos:
                print("⚠️ Produtos com estoque baixo:")

                for id_, nome, categoria, qtd, preco in produtos:
                    print(f"{id_:<5} {nome:<20} {categoria:<15} {qtd:<5} R$ {preco:<10.2f}")
            else:
                print("Nenhum produto com estoque baixo.")

        except sqlite3.Error as e:
            print(f"❌ Erro ao verificar estoque: {e}")

    def close(self):
        try:
            self.cursor.close()
            self.conexao.close()
            print("✅ Banco fechado!")
        except sqlite3.Error as e:
            print(f"❌ Erro ao fechar banco: {e}")


def trata_input(msg, especial=False):
    while True:
        dado = input(msg)
        if not dado:
            print("Digite algo...")
            continue

        if especial and dado not in "1234560":
            print("Digite apenas valores de 0 até 6!")
            continue

        return dado


def trata_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um valor numérico inteiro")


def trata_float(msg):
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("Digite apenas números")
            continue


def main():
    banco = BancoCadastro()
    banco.create_table()
    opcoes = [
        ['1', "Cadastrar produto"],
        ['2', "Listar produtos"],
        ['3', "Atualizar quantidade"],
        ['4', "Remover produto"],
        ['5', "Buscar por categoria"],
        ['6', "Alerta de estoque baixo"],
        ['0', "Sair"],
    ]

    for opc, item in opcoes:
        print(f"[{opc}] {item}")

    while True:
        opc = trata_input(">> ", especial=True)

        match opc:
            case "1":
                nome = trata_input("Nome do produto: ")
                categoria = trata_input("Categoria: ")
                qtd = trata_int("Quantidade: ")
                preco = trata_float("Preço: ")

                banco.create(nome, categoria, qtd, preco)
            case "2":
                banco.read()
            case "3":
                _id = trata_int("ID do produto: ")
                nova_qtd = trata_int("Nova Quantidade: ")
                banco.update_qtd(_id, nova_qtd)
            case "4":
                _id = trata_int("ID do produto que vai remover: ")
                banco.delete(_id)
            case "5":
                categoria = trata_input("Categoria: ")
                banco.buscar_por_categoria(categoria)
            case "6":
                limite = trata_int("Limite: ")
                banco.alerta_estoque_baixo(limite)
            case "0":
                print("Fim da execução!")
                banco.close()
                break
            case _:
                print("Opção inválida!")

        print()


if __name__ == "__main__":
    main()
