from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self):
        super().__init__()


    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso

