def analisar_status(status):
    tabela = {
        2: "sucessos",
        4: "erros_cliente",
        5: "erros_servidor"
    }

    resultado = {
        "sucessos": 0,
        "erros_cliente": 0,
        "erros_servidor": 0,
        "total": 0
    }

    for codigo in status:
        classe = codigo // 100

        categoria = tabela.get(classe, "outros")

        resultado[categoria] += 1
        resultado["total"] += 1

    return resultado


print(analisar_status([200, 404, 200, 500, 200, 404, 503, 200]))
print()
print(analisar_status([201, 204, 400, 502]))
print()
print(analisar_status([]))
print()
print(analisar_status([200]))
