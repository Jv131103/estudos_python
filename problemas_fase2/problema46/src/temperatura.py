import math


def controlar_temperatura(temperatura):
    if not isinstance(temperatura, (float, int)) or isinstance(temperatura, bool):
        raise ValueError("Tipo inválido para temperatura. Só é aceito INT ou FLOAT")

    if not math.isfinite(temperatura):
        raise ValueError("Temperatura deve ser um número finito")

    tabela = (
        ["Temperatura normal", float('-inf'), 25],
        ["Ligar ventilação", 25, 35],
        ["ALERTA: temperatura crítica!", 35, float("inf")]
    )

    for status, valx, valy in tabela:
        if valx <= temperatura < valy:
            return status

    return "Não identificado!"


if __name__ == "__main__":
    testes = (
        [20, "Temperatura normal"],
        [25, "Ligar ventilação"],
        [34, "Ligar ventilação"],
        [35, "ALERTA: temperatura crítica!"]
    )

    for temperatura, status in testes:
        resultado = controlar_temperatura(temperatura)
        assert resultado == status, f"Inválido para temperatura {temperatura}\nRETORNO: {resultado} | ESPERADO: {status}"
