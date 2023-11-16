class Cargo():
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario_bruto(self, outros_acrescimos=0):
        return self.salario_base + outros_acrescimos