def inverter_dicionario(d):

    new_d = {}

    for key, value in d.items():
        new_d[value] = key

    return new_d


d = {"a": 1, "b": 2, "c": 3}
print(inverter_dicionario(d))
