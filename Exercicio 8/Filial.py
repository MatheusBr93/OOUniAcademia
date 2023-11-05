class Filial:
    def __init__(self, nome):
        self.__nome = nome
        self.__empresa = ""
        self.__funcionarios = []

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEmpresa(self, empresa):
        self.__empresa = empresa

    def getEmpresa(self):
        return self.__empresa

    def adicionarFuncionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def listarFuncionarios(self):
        return self.__funcionarios
