"""
Crie factory usando Enum.
"""

from abc import ABC, abstractmethod
from enum import Enum


class OptionIaError(Exception):
    pass


class ExecutarAgente(Enum):
    CHATGPT = 1
    GEMINI = 2
    DEEPSEEK = 3
    CLOUD = 4
    COPILOT = 5
    PERPLEXITY = 6
    CANVA = 7


class UsarIA(ABC):
    @abstractmethod
    def executar(self):
        pass


class ChatGpt(UsarIA):
    def executar(self):
        print("Executando GPT...")


class Gemini(UsarIA):
    def executar(self):
        print("Executando GEMINI...")


class DeepSeek(UsarIA):
    def executar(self):
        print("Executando DEEP SEEK...")


class Cloud(UsarIA):
    def executar(self):
        print("Executando CLOUD...")


class Copilot(UsarIA):
    def executar(self):
        print("Executando COPILOT...")


class Perplexity(UsarIA):
    def executar(self):
        print("Executando PERPLEXITY...")


class Canva(UsarIA):
    def executar(self):
        print("Executando CANVA...")


class OpcaoIA:
    _tipos = {
        ExecutarAgente.CHATGPT: ChatGpt,
        ExecutarAgente.GEMINI: Gemini,
        ExecutarAgente.DEEPSEEK: DeepSeek,
        ExecutarAgente.CLOUD: Cloud,
        ExecutarAgente.COPILOT: Copilot,
        ExecutarAgente.PERPLEXITY: Perplexity,
        ExecutarAgente.CANVA: Canva
    }

    @classmethod
    def criar(cls, ia_escolhida: ExecutarAgente) -> UsarIA:
        classe = cls._tipos.get(ia_escolhida)
        if not classe:
            raise OptionIaError(f"{ia_escolhida} não existe")
        return classe()


ia = OpcaoIA.criar(ExecutarAgente.CHATGPT)
ia.executar()
