"""
Crie uma classe que implemente __call__.
"""

from typing import Any


class Automation:
    def acessar(self, url):
        print(f"Acessando url: {url}")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Executando dados....")
        self.acessar(*args, **kwds)


aut = Automation()
aut("https://google.com")
