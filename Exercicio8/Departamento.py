class Departamento:
    def __init__(self, departamento):
        self.__departamento = departamento
        self.__funcionariosAlocados = []
        self.__chefe = ""

    def setDepartamento(self, departamento):
        self.__departamento = departamento

    def getDepartamento(self):
        return self.__departamento

    def setChefe(self, chefe):
        self.__chefe = chefe

    def getChefe(self):
        return self.__chefe

    def adicionarFuncionario(self, funcionario):
        self.__funcionariosAlocados.append(funcionario)

    def listarFuncionarios(self):
        return self.__funcionariosAlocados
