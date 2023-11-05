class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__filiais = []
        self.__departamentos = []
        self.__diretor = ""

    def setDiretor(self, diretor):
        self.__diretor = diretor

    def getDiretor(self):
        return self.__diretor

    def adicionarFilial(self, filial):
        self.__filiais.append(filial)

    def listarFiliais(self):
        return self.__filiais

    def adicionarDepartamento(self, departamento):
        self.__departamentos.append(departamento)

    def listarDepartamentos(self):
        return self.__departamentos

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
