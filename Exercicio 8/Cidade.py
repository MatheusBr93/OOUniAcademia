class Cidade:
    def __init__(self, nome):
        self.__nome = nome
        self.__filiais = []

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def adicionarFilial(self, filial):
        self.__filiais.append(filial)

    def listarFiliais(self):
        return self.__filiais
