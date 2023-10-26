class Curso:
    def __init__(self):
        self.__id = 0
        self.__descricao = ""
        self.__disciplinas = []
        self.__professores = []

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_disciplinas(self):
        return self.__disciplinas

    def set_disciplinas(self, disciplinas):
        self.__disciplinas = disciplinas

    def get_professores(self):
        return self.__professores

    def set_professores(self, professores):
        self.__professores = professores