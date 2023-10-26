from Aluno import Aluno
from Turma import Turma

class Diario:
    def __init__(self):
        self.__v1 = 0
        self.__v2 = 0
        self.__vS = 0
        self.__vT = 0
        self.__faltas = 0
        self.__Aluno = Aluno()
        self.__turma = Turma()

    def get_v1(self):
        return self.__v1

    def set_v1(self, v1):
        self.__v1 = v1

    def get_v2(self):
        return self.__v2

    def set_v2(self, v2):
        self.__v2 = v2

    def get_vS(self):
        return self.__vS

    def set_vS(self, vS):
        self.__vS = vS

    def get_vT(self):
        return self.__vT

    def set_vT(self, vT):
        self.__vT = vT

    def get_faltas(self):
        return self.__faltas

    def set_faltas(self, faltas):
        self.__faltas = faltas

    def get_Aluno(self):
        return self.__Aluno

    def set_Aluno(self, Aluno):
        self.__Aluno = Aluno

    def get_turma(self):
        return self.__turma

    def set_turma(self, turma):
        self.__turma = turma