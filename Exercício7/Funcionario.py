class Funcionario:
    def __int__(self):
        self.__nome = ""
        self.__salarioBruto = 0.0
        self.__totalDeAcrescimos = 0.0
        self.__totalDeDescontos = 0.0
        self.__salarioLiquido = 0.0

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.__salarioBruto

    def setTotalDeAcrescimos(self, totalDeAcrescimos):
        self.__totalDeAcrescimos = totalDeAcrescimos

    def getTotalDeAcrescimos(self):
        return self.__totalDeAcrescimos

    def setTotalDeDescontos(self, totalDeDescontos):
        self.__totalDeDescontos = totalDeDescontos

    def getTotalDeDescontos(self):
        return self.__totalDeDescontos

    def getSalarioLiquido(self):
        salarioLiquido = self.__salarioBruto + self.__totalDeAcrescimos - self.__totalDeDescontos
        return salarioLiquido
