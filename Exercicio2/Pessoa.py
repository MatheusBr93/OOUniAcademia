class Pessoa:
    def __init__(self):
        self.__nome = ""

    def setNome(self, nome):
        self.__nome = nome
        return print("Nome definido como: " + self.__nome)

    def getNome(self):
        return self.__nome



