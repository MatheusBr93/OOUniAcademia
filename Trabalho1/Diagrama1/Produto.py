class Produto:
    def __init__(self):
        self.__id = 0
        self.__codigo = 0
        self.__descricao = ""

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao
