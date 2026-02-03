import os
import platform
import sys

try:
    import psutil
except ImportError:
    psutil = None

print("=== DIAGNÓSTICO ===")
print("SO:", platform.system(), platform.release())
print("Python:", platform.python_version())
print("Pasta atual:", os.getcwd())
print("Args:", sys.argv)

if psutil:
    print("CPU %:", psutil.cpu_percent(interval=1))
    print("RAM %:", psutil.virtual_memory().percent)
else:
    print("psutil não instalado. Rode: pip install psutil")
