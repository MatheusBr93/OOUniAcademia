class Estado:
    def __init__(self):
        self.__nome = ""
        self.__cidade = []
        self.__naturalidade = ""

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def adicionarCidade(self, cidade):
        self.__cidade.append(cidade)

    def removerCidade(self, cidade):
        self.__cidade.append(cidade)

    def __str__(self):
        return self.getNome()


