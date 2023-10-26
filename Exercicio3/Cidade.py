class Cidade:
    def __init__(self):
        self.__nome = ""
        self.__pessoas = []
        self.__escolas = []

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def adicionarPessoa(self, nome_da_pessoa):
        self.__pessoas.append(nome_da_pessoa)

    def removerPessoa(self, nome_da_pessoa):
        self.__pessoas.remove(nome_da_pessoa)

    def setEstado(self, estado):
        self.__estado = estado

    def getEstado(self):
        return self.__estado

    def adicionarEscolas(self, nome_da_escola):
        self.__escolas.append(nome_da_escola)

    def removerEscolas(self, nome_da_escola):
        self.__escolas.remove(nome_da_escola)