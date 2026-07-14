logs = [
    "ERRO",
    "INFO",
    "INFO",
    "WARN",
    "ERRO",
    "DEBUG",
]

clusters = {}

for log in logs:
    clusters.setdefault(log, []).append(log)

print(clusters)
