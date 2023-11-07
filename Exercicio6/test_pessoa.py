import pytest
from Pessoa import Pessoa

def test_calcula_imc_masculino():
    pessoa = Pessoa("Masculino", 70, 1.75)
    assert pessoa.calcularIMC() == "Peso normal"

def test_calcula_imc_feminino():
    pessoa = Pessoa("Feminino", 60, 1.65)
    assert pessoa.calcularIMC() == "Dentro do Padrão"

def test_calcula_imc_sexo_desconhecido():
    pessoa = Pessoa("Outro", 70, 1.75)
    assert pessoa.calcularIMC() == "Sexo não reconhecido"

if __name__ == "__main__":
    pytest.main()