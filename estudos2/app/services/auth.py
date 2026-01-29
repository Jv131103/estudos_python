from ..core.config import DEBUG


def iniciar_modo_debug():
    if DEBUG:
        print("ATIVANDO DEBUG")
        return True
    return False
