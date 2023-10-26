from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()
        self.__matricula = ""
        self.__anoInicio = 0
        self.__semestreInicio = 0
        self.__situacoes = []
        self.__diarios = []

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_anoInicio(self):
        return self.__anoInicio

    def set_anoInicio(self, ano):
        self.__anoInicio = ano

    def get_semestreInicio(self):
        return self.__semestreInicio

    def set_semestreInicio(self, semestre):
        self.__semestreInicio = semestre

    def get_situacoes(self):
        return self.__situacoes

    def get_diarios(self):
        return self.__diarios
