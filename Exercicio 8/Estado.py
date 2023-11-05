class Estado:
    def __init__(self, nome):
        self.__nome = nome
        self.__cidades = []

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def adicionarCidade(self, cidade):
        self.__cidades.append(cidade)

    def listarCidades(self):
        return self.__cidades
