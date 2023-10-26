from Escolaridade import Escolaridade
from Cidade import Cidade
class Pessoa:
    def __init__(self):
        self.__cidade = Cidade()
        self.__escolaridade = Escolaridade()
        self.__nome = ""

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getCidade(self):
        return self.__cidade

    def setEscolaridade(self, nivel):
        self.__escolaridade = nivel

    def getEscolaridade(self):
        return self.__escolaridade
