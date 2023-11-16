from datetime import datetime

class Funcionario():
    def __init__(self, nome, cargo, salario_bruto, data_nascimento, dependentes=[]):
        self.nome = nome
        self.cargo = cargo
        self.salario_bruto = salario_bruto
        self.data_nascimento = data_nascimento
        self.dependentes = dependentes

    def calcular_salario_liquido(self, ano, mes):
        salario_liquido = self.salario_bruto
        for dependente in self.dependentes:
            if dependente.get_idade(ano, mes) < 18:
                salario_liquido += 100.00
