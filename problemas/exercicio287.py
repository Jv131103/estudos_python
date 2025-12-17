def sequencia_controlada(n):
    dados = {
        "fizz": [],
        "buzz": [],
        "FizzBuzz": []
    }
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            dados["FizzBuzz"].append(i)
        elif i % 3 == 0:
            dados["fizz"].append(i)
        elif i % 5 == 0:
            dados["buzz"].append(i)

    return dados


print(sequencia_controlada(20))
