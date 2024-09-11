from abc import ABC, abstractmethod
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        
    @classmethod
    def salario_final(self) -> float:
        pass
    
    def __str__(self) -> str:
        return (
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\nDados do endereço: {self.endereco}"
                )