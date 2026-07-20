from dataclasses import dataclass
from typing import List


@dataclass
class RegraIngresso:
    dia_min: int
    dia_max: int
    hora_min: int
    hora_max: int
    tipo_sala: str
    categoria_cliente: str
    preco_final: float


DIAS_SEMANA = {
    "seg": 0, "ter": 1, "qua": 2, "qui": 3,
    "sex": 4, "sab": 5, "dom": 6
}


TABELA_REGRAS: List[RegraIngresso] = [
    RegraIngresso(0, 3, 0, 14, "qualquer", "qualquer", 12.00),
    RegraIngresso(0, 3, 15, 23, "normal", "comum", 22.00),
    RegraIngresso(0, 3, 15, 23, "normal", "estudante", 11.00),
    RegraIngresso(0, 3, 15, 23, "normal", "idoso", 11.00),
    RegraIngresso(0, 3, 15, 23, "3d/imax", "comum", 32.00),
    RegraIngresso(0, 3, 15, 23, "3d/imax", "estudante", 16.00),
    RegraIngresso(0, 3, 15, 23, "3d/imax", "idoso", 16.00),
    RegraIngresso(4, 6, 0, 23, "normal", "comum", 28.00),
    RegraIngresso(4, 6, 0, 23, "normal", "estudante", 14.00),
    RegraIngresso(4, 6, 0, 23, "normal", "idoso", 14.00),
    RegraIngresso(4, 6, 0, 23, "3d/imax", "comum", 38.00),
    RegraIngresso(4, 6, 0, 23, "3d/imax", "estudante", 19.00),
    RegraIngresso(4, 6, 0, 23, "3d/imax", "idoso", 19.00),
]


def precificar_ingresso(dia_texto: str, hora: int, sala: str, categoria: str) -> float:
    dia_num = DIAS_SEMANA.get(dia_texto.lower().strip())
    sala_norm = sala.lower().strip()
    cat_norm = categoria.lower().strip()

    if dia_num is None:
        raise ValueError("Dia da semana inválido. Use seg, ter, qua, qui, sex, sab ou dom.")

    for regra in TABELA_REGRAS:
        if not (regra.dia_min <= dia_num <= regra.dia_max):
            continue

        if not (regra.hora_min <= hora <= regra.hora_max):
            continue

        if regra.tipo_sala != "qualquer" and regra.tipo_sala != sala_norm:
            continue

        if regra.categoria_cliente != "qualquer" and regra.categoria_cliente != cat_norm:
            continue

        return regra.preco_final

    raise ValueError("Nenhuma regra de preço encontrada para esta combinação.")


# --- Testes Práticos ---
if __name__ == "__main__":
    print(f"Sessão 1: R$ {precificar_ingresso('qua', 13, '3d/imax', 'estudante'):.2f}")

    print(f"Sessão 2: R$ {precificar_ingresso('qui', 19, 'normal', 'comum'):.2f}")

    print(f"Sessão 3: R$ {precificar_ingresso('dom', 16, '3d/imax', 'idoso'):.2f}")
