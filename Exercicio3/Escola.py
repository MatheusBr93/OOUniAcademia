class Escola:
    def __init__(self):
        self.__nome = ""
        self.__diretor = ""
    def setNome(self,nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def getDiretor(self):
        return self.__diretor

    def setDiretor(self, professor):
        self.__diretor = professor

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getCidade(self):
        return self.__cidade