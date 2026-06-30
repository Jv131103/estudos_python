lista_emails = ["ana@email.com", "bruno@email.com", "carlos@email.com"]

# 'instancia_email' é a nossa variável de iteração.
# Na volta 1 ela vale "ana...", na volta 2 vale "bruno...", etc.
for instancia_email in lista_emails:
    # Processamos o elemento focado neste exato ciclo
    usuario = instancia_email.split("@")[0]
    print(f"Usuário processado: {usuario}")
