"""
Crie duas classes diferentes com método processar
e uma função que aceite qualquer uma.
"""

import psutil


class ProcessoCPU:
    def processar(self):
        print("CPU %:", psutil.cpu_percent(interval=1))


class ProcessoRAM:
    def processar(self):
        print("RAM %:", psutil.virtual_memory().percent)


def processar_maquina(processo):
    processo.processar()


processos = [ProcessoCPU(), ProcessoRAM()]

for p in processos:
    processar_maquina(p)
