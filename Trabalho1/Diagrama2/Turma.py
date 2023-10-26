from Instituicao import Instituicao
from Disciplina import Disciplina
from Professor import Professor

class Turma:
    def __init__(self,):
        self.__id = 0
        self.__descricao = 0
        self.__ano = 0
        self.__semestre = 0
        self.__Instituicao = Instituicao()
        self.__Disciplina = Disciplina()
        self.__Professor = Professor()
        self.__diarios = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_semestre(self):
        return self.__semestre

    def set_semestre(self, semestre):
        self.__semestre = semestre

    def get_Instituicao(self):
        return self.__Instituicao

    def set_Instituicao(self, Instituicao):
        self.__Instituicao = Instituicao

    def get_Disciplina(self):
        return self.__Disciplina

    def set_Disciplina(self, Disciplina):
        self.__Disciplina = Disciplina

    def get_Professor(self):
        return self.__Professor

    def set_Professor(self, Professor):
        self.__Professor = Professor

    def get_diarios(self):
        return self.__diarios