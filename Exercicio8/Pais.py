class Pais:
    def __init__(self, nome):
        self.__nome = nome
        self.__estados = []
        self.__sede = ""

    def setSede(self, sede):
        self.__sede = sede

    def getSede(self):
        return self.__sede

    def adicionarEstado(self, estado):
        self.__estados.append(estado)

    def listarEstados(self):
        return self.__estados

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
