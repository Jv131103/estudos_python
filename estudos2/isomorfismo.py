def sao_isomorficas(s, t):
    # Passo 1: Se o tamanho for diferente, a estrutura já é diferente!
    if len(s) != len(t):
        return False

    map_s_para_t = {}
    map_t_para_s = {}

    # Passo 2: Percorrer as duas strings juntas, caractere por caractere
    for char_s, char_t in zip(s, t):
        # Verifica o mapeamento de S para T
        if char_s in map_s_para_t:
            if map_s_para_t[char_s] != char_t:
                return False  # Opa! A letra de S tentou apontar para outra letra de T
        else:
            map_s_para_t[char_s] = char_t

        # Verifica o mapeamento de T para S (A volta)
        if char_t in map_t_para_s:
            if map_t_para_s[char_t] != char_s:
                return False  # Opa! A letra de T tentou apontar para outra letra de S
        else:
            map_t_para_s[char_t] = char_s

    return True


# Exemplo 1: "egg" e "add" (Padrão 1-2-2)
# e -> a, g -> d. Na última letra, 'g' já aponta para 'd', que bate com 'd'.
print(sao_isomorficas("egg", "add"))  # True

# Exemplo 2: "foo" e "bar" (Padrão 1-2-2 vs 1-2-3)
# f -> b, o -> a. Na última letra, 'o' tenta apontar para 'r', mas já apontava para 'a'! Quebrou.
print(sao_isomorficas("foo", "bar"))  # False

# Exemplo 3: "paper" e "title" (Padrão 1-2-1-3-4)
# p->t, a->i, p->t (ok), e->l, r->e
print(sao_isomorficas("paper", "title"))  # True

# Exemplo 4: "badc" e "baba" (Mapeamento duplicado)
# b->b, a->a, d->b (Opa! 'b' em T já está sendo usado pelo 'b' de S! Traição detectada pelo map_t_para_s)
print(sao_isomorficas("badc", "baba"))  # False
