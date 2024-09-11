import os
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.cliente import Cliente

os.system("cls || clear")

aluno = Pessoa("Marta", 22, Sexo.FEMININO, 
               Endereco("Rua A", "33", UnidadeFederativa.BAHIA))
print(aluno)

cliente_1 = Cliente("Jose", 42, Sexo.MASCULINO, 
               Endereco("Rua B", "35", UnidadeFederativa.RIO_DE_JANEIRO))
print(cliente_1)