produto1 = {
    'nome': 'produto1',
    'tipo': 'categoriaA',
    'valor': '50.5',
    'fornecedor': 'ABCD',
}

print(f"Produto antes: {produto1}")

produto1['valor'] = 99.98  # type: ignore
print(f"Produto agora: {produto1}")
