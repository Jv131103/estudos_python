"""
Faça um “executor de comando”:

    recebe um comando por argumentos (sys.argv)

    roda via subprocess.run

    imprime stdout, stderr e returncode

    se CTRL+C, encerra limpinho com signal

(Módulos: sys, subprocess, signal)

"""

import signal
import subprocess
import sys


# 1. Tratamento de CTRL+C
def sair_limpo(sig, frame):
    print("\nCTRL+C detectado. Encerrando com segurança.")
    sys.exit(0)


signal.signal(signal.SIGINT, sair_limpo)

# 2. Verificar argumentos
if len(sys.argv) < 2:
    print("Uso: python executor.py COMANDO [ARGS...]")
    sys.exit(1)

# 3. Capturar comando
comando = sys.argv[1:]

# 4. Executar comando
try:
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True
    )

    print("===== STDOUT =====")
    print(resultado.stdout)

    print("===== STDERR =====")
    print(resultado.stderr)

    print("===== RETURN CODE =====")
    print(resultado.returncode)

except FileNotFoundError:
    print("Comando não encontrado.")
