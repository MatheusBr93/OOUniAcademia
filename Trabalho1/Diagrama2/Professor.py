from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__matricula = 0
        self.__titulacaoMaxima = 0
        self.__turmas = []
        self.__cursos = []

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_titulacaoMaxima(self):
        return self.__titulacaoMaxima

    def set_titulacaoMaxima(self, titulacaoMaxima):
        self.__titulacaoMaxima = titulacaoMaxima

    def get_turmas(self):
        return self.__turmas

    def get_cursos(self):
        return self.__cursos
