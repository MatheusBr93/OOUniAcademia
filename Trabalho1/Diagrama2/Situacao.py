class Situacao:
    def __init__(self):
        self.__situacao = 0
        self.__anoSemestre = 0
        self.__alunos = []

    def get_situacao(self):
        return self.__situacao

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def get_anoSemestre(self):
        return self.__anoSemestre

    def set_anoSemestre(self, anoSemestre):
        self.__anoSemestre = anoSemestre

    def get_alunos(self):
        return self.__alunos

    def set_alunos(self, alunos):
        self.__alunos = alunos

