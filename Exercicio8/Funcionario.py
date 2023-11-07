class Funcionario:
    def __init__(self, nome, escolaridade, empresa):
        self.__nome = nome
        self.__escolaridade = escolaridade
        self.__empresa = empresa
        self.__coordenador = ""

    def setCoordenador(self, coordenador):
        self.__coordenador = coordenador

    def getCoordenador(self):
        return self.__coordenador

    def getNome(self):
        return self.__nome

    def getEscolaridade(self):
        return self.__escolaridade

    def getEmpresa(self):
        return self.__empresa

    def setNome(self, nome):
        self.__nome = nome

    def setEscolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    def setEmpresa(self, empresa):
        self.__empresa = empresa
