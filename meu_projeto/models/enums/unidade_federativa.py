from enum import Enum

# snake_case
# class unidade_federativa:

# Pascal Case
class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SAO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")

    def __init__(self, nome: str, sigla: str) -> None:
        self.nome = nome
        self.sigla = sigla

