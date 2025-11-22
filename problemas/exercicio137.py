nomes = [
    '',
    'Roberto Carlos',
    'Tom Jobim',
    'Jorge Amado',
    'Machado de Assis',
    'Zé Ramalho',
    'Elba Ramalho',
    '',
    '',
    [],
    ()
]


nomes_limpos = list(filter(lambda nome: nome, nomes))
print(nomes_limpos)


ramalhos = list(
    filter(lambda nome: "Ramalho" in nome, nomes_limpos)
)
print(ramalhos)
